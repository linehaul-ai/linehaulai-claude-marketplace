#!/usr/bin/env python3
"""Parse Swagger 2.0 spec into per-endpoint markdown reference files.

Each output file is self-contained: endpoint description, parameter table,
fully resolved response schema with nested model fields inlined.
"""

import json
import os
import re
from pathlib import Path

SPEC = Path(".firecrawl/mcp-swagger-spec.json")
OUT_DIR = Path("plugins/mycarrierpackets-api/skills/mycarrierpackets-api/references/endpoints")

# Endpoint domain grouping for the index + cross-linking.
GROUPS = {
    "Carrier Data": [
        "PreviewCarrier", "GetCarrierData", "GetCarrierContacts",
        "GetCarrierRiskAssessment", "GetCarrierIncidentReports",
        "GetCarrierVINVerifications", "FindAssociatedCarriers",
    ],
    "Invitations & Verification": [
        "EmailPacketInvitation", "CompletedPackets",
        "RequestUserVerification", "RequestVINVerification",
    ],
    "Monitoring": [
        "RequestMonitoring", "CancelMonitoring",
        "MonitoredCarriers", "MonitoredCarrierData",
        "GetMonitoredCarrierContactsData",
        "GetMonitoredCarriersRiskAssessment", "CarriersChanges",
    ],
    "Block / Unblock": ["BlockCarrier", "UnblockCarrier", "BlockedCarriers"],
    "Documents": ["GetDocument"],
    "Factoring": ["GetUpdatedFactoringCompanies"],
}

# Endpoints that return pagination data.
PAGINATION_HEADER = {"MonitoredCarriers", "BlockedCarriers", "CarriersChanges"}
PAGINATION_BODY = {"MonitoredCarrierData"}


def short(name: str) -> str:
    """Last segment of dotted .NET type name."""
    return name.split(".")[-1] if name else name


def kebab(name: str) -> str:
    """CamelCase -> kebab-case."""
    s = re.sub(r"(.)([A-Z][a-z]+)", r"\1-\2", name)
    s = re.sub(r"([a-z0-9])([A-Z])", r"\1-\2", s)
    return s.lower()


def short_op(op_id: str) -> str:
    return op_id.split("_", 1)[1] if "_" in op_id else op_id


class SchemaResolver:
    def __init__(self, definitions):
        self.definitions = definitions

    def fmt_type(self, schema):
        """Inline type description for a property schema."""
        if not schema:
            return "any"
        if "$ref" in schema:
            return short(schema["$ref"].split("/")[-1])
        t = schema.get("type")
        fmt = schema.get("format")
        if t == "array":
            return f"Array[{self.fmt_type(schema.get('items', {}))}]"
        if t == "integer":
            return f"integer ({fmt})" if fmt else "integer"
        if t == "number":
            return f"number ({fmt})" if fmt else "number"
        if t == "boolean":
            return "boolean"
        if t == "string":
            if fmt:
                return f"string ({fmt})"
            return "string"
        if t == "object":
            return "object"
        if "enum" in schema:
            return f"enum {schema['enum']}"
        return t or "any"

    def model_refs(self, schema, refs):
        """Collect all $ref names reachable from this schema."""
        if not isinstance(schema, dict):
            return
        if "$ref" in schema:
            name = schema["$ref"].split("/")[-1]
            if name not in refs:
                refs.add(name)
                if name in self.definitions:
                    self.model_refs(self.definitions[name], refs)
            return
        for v in schema.values():
            if isinstance(v, dict):
                self.model_refs(v, refs)
            elif isinstance(v, list):
                for x in v:
                    self.model_refs(x, refs)

    def render_model(self, name):
        """Render a model definition as a markdown table. Returns (md, nested_refs)."""
        defn = self.definitions.get(name)
        if not defn:
            return f"(definition not found: `{name}`)\n", set()

        out = [f"**`{short(name)}`**"]
        if defn.get("description"):
            out.append("")
            out.append(defn["description"])
        props = defn.get("properties", {})
        required = set(defn.get("required", []))

        if not props:
            out.append("")
            out.append(f"_No properties defined. Raw type: `{defn.get('type','object')}`_")
            return "\n".join(out) + "\n", set()

        out.append("")
        out.append("| Field | Type | Req | Description |")
        out.append("|-------|------|-----|-------------|")
        nested = set()
        for pname, pschema in props.items():
            ptype = self.fmt_type(pschema)
            req = "yes" if pname in required else ""
            desc = (pschema.get("description") or "").replace("\n", " ").replace("|", "\\|").strip()
            # Enum hint
            if "enum" in pschema:
                desc = (desc + f" (enum: {pschema['enum']})").strip()
            out.append(f"| `{pname}` | `{ptype}` | {req} | {desc} |")
            # Collect nested refs
            sub_refs = set()
            self.model_refs(pschema, sub_refs)
            nested |= sub_refs

        nested -= {name}
        return "\n".join(out) + "\n", nested


def render_endpoint(path, method, op, resolver):
    op_id = op["operationId"]
    name = short_op(op_id)
    summary = op.get("summary", "").strip()

    lines = []
    lines.append(f"# {name}")
    lines.append("")
    lines.append(f"`{method.upper()} {path}`")
    lines.append("")
    if summary:
        lines.append(summary)
        lines.append("")

    # Parameters
    params = op.get("parameters", [])
    query = [p for p in params if p.get("in") == "query"]
    header = [p for p in params if p.get("in") == "header"]
    body = [p for p in params if p.get("in") == "body"]

    lines.append("## Parameters")
    lines.append("")

    if query:
        lines.append("**Query string:**")
        lines.append("")
        lines.append("| Name | Type | Req | Description |")
        lines.append("|------|------|-----|-------------|")
        for p in query:
            ptype = p.get("type", "")
            if p.get("format"):
                ptype = f"{ptype} ({p['format']})"
            if ptype == "array":
                ptype = f"Array[{p.get('items',{}).get('type','')}]"
            req = "yes" if p.get("required") else ""
            desc = (p.get("description") or "").replace("\n", " ").replace("|", "\\|").strip()
            if "enum" in p:
                desc = (desc + f" (enum: {p['enum']})").strip()
            lines.append(f"| `{p['name']}` | `{ptype}` | {req} | {desc} |")
        lines.append("")

    if header:
        lines.append("**Headers:**")
        lines.append("")
        lines.append("| Name | Required | Description |")
        lines.append("|------|----------|-------------|")
        for p in header:
            req = "yes" if p.get("required") else ""
            desc = (p.get("description") or "").strip()
            lines.append(f"| `{p['name']}` | {req} | {desc} |")
        lines.append("")
        lines.append("> All endpoints require `Authorization: bearer <access_token>`.")
        lines.append("")

    if body:
        lines.append("**Body:**")
        lines.append("")
        for p in body:
            lines.append(f"- `{p['name']}` ({'required' if p.get('required') else 'optional'})")
            schema = p.get("schema")
            if schema:
                lines.append("")
                lines.append("```json")
                lines.append(json.dumps(schema, indent=2))
                lines.append("```")
        lines.append("")

    # Pagination flag
    if name in PAGINATION_HEADER:
        lines.append("> **Pagination:** returned in `X-Pagination` response header as JSON: `{pageNumber, pageSize, totalPages, totalCount}`.")
        lines.append("")
    elif name in PAGINATION_BODY:
        lines.append("> **Pagination:** returned in response body as `pageNumber`, `pageSize`, `totalPages`, `totalCount` fields.")
        lines.append("")

    # Response
    lines.append("## Response (200)")
    lines.append("")
    resp = op.get("responses", {}).get("200", {})
    resp_desc = resp.get("description", "").strip()
    if resp_desc and resp_desc != "OK":
        lines.append(resp_desc)
        lines.append("")

    schema = resp.get("schema")
    if not schema:
        lines.append("_Empty response body._")
        lines.append("")
    else:
        # Top-level shape
        top_type = resolver.fmt_type(schema)
        lines.append(f"**Returns:** `{top_type}`")
        lines.append("")

        # Resolve top-level model
        top_ref = None
        if schema.get("type") == "array":
            top_ref = schema.get("items", {}).get("$ref")
        else:
            top_ref = schema.get("$ref")

        models_to_render = []
        seen = set()
        if top_ref:
            top_name = top_ref.split("/")[-1]
            models_to_render.append(top_name)
            # Pre-collect all nested refs reachable from the top model
            all_refs = set()
            resolver.model_refs(resolver.definitions.get(top_name, {}), all_refs)
            for r in sorted(all_refs):
                if r != top_name and r not in seen:
                    models_to_render.append(r)

        # Render each model
        for i, m in enumerate(models_to_render):
            if m in seen:
                continue
            seen.add(m)
            md, _ = resolver.render_model(m)
            if i == 0:
                lines.append(f"### Top-level: {short(m)}")
            else:
                lines.append(f"### Nested model: {short(m)}")
            lines.append("")
            lines.append(md)
            lines.append("")

    # Cross-references
    lines.append("## See also")
    lines.append("")
    group = next((g for g, ops in GROUPS.items() if name in ops), None)
    if group:
        siblings = [o for o in GROUPS[group] if o != name]
        if siblings:
            lines.append(f"Related endpoints in **{group}**:")
            lines.append("")
            for s in siblings:
                lines.append(f"- [{s}](./{kebab(s)}.md)")
            lines.append("")
    lines.append("- [Endpoint INDEX](./INDEX.md)")
    lines.append("- [SKILL.md](../../SKILL.md) — workflow guidance, auth, pagination, error handling")
    lines.append("- [TMS-INTEGRATION.md](../TMS-INTEGRATION.md) — official numbered integration workflow")
    lines.append("")

    return "\n".join(lines)


def render_index(spec, by_op):
    lines = ["# MyCarrierPackets API — Endpoint Index", ""]
    lines.append(f"**Base URL:** `https://{spec.get('host','api.mycarrierpackets.com')}`")
    lines.append(f"**Version:** {spec.get('info',{}).get('version','v1')}")
    lines.append(f"**Auth:** `Authorization: bearer <access_token>` (OAuth2 password grant — see [SKILL.md](../../SKILL.md#authentication))")
    lines.append(f"**Format:** JSON default; XML via `Accept: text/xml`")
    lines.append("")
    lines.append(f"All endpoints use `POST`. {len(by_op)} total endpoints across {len(GROUPS)} domains.")
    lines.append("")

    for group, ops in GROUPS.items():
        lines.append(f"## {group}")
        lines.append("")
        lines.append("| Endpoint | Path | Summary |")
        lines.append("|----------|------|---------|")
        for op_name in ops:
            op = by_op.get(op_name)
            if not op:
                continue
            path = op["_path"]
            summary = (op.get("summary") or "").replace("|", "\\|").replace("\n", " ").strip()
            # Strip markdown bold from summary for table
            summary = re.sub(r"\*\*([^*]+)\*\*", r"\1", summary)
            tags = []
            if op_name in PAGINATION_HEADER:
                tags.append("📄 paginated (header)")
            elif op_name in PAGINATION_BODY:
                tags.append("📄 paginated (body)")
            if tags:
                summary = f"{summary} _{', '.join(tags)}_"
            lines.append(f"| [{op_name}](./{kebab(op_name)}.md) | `{path}` | {summary} |")
        lines.append("")

    lines.append("## See also")
    lines.append("")
    lines.append("- [SKILL.md](../../SKILL.md) — auth, workflows, pagination, error handling")
    lines.append("- [TMS-INTEGRATION.md](../TMS-INTEGRATION.md) — official numbered integration workflow")
    lines.append("")
    return "\n".join(lines)


def main():
    spec = json.load(open(SPEC))
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    resolver = SchemaResolver(spec.get("definitions", {}))

    # Flatten operations
    by_op = {}
    for path, methods in spec["paths"].items():
        for method, op in methods.items():
            op_name = short_op(op["operationId"])
            op = dict(op)
            op["_path"] = path
            op["_method"] = method
            by_op[op_name] = op

    # Render each endpoint
    written = []
    for op_name, op in by_op.items():
        md = render_endpoint(op["_path"], op["_method"], op, resolver)
        fname = OUT_DIR / f"{kebab(op_name)}.md"
        fname.write_text(md)
        written.append((op_name, fname.name, len(md)))

    # Index
    (OUT_DIR / "INDEX.md").write_text(render_index(spec, by_op))

    print(f"Wrote {len(written)} endpoint files + INDEX.md to {OUT_DIR}")
    for op_name, fn, size in sorted(written):
        print(f"  {size:6d}  {fn}")


if __name__ == "__main__":
    main()
