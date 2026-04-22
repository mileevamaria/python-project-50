def _format_str_value(value, depth: int) -> str:  # noqa: C901
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    elif not isinstance(value, dict):
        return str(value)
    
    indent = ' ' * (depth * 4)
    lines = ['{']
    for k, v in value.items():
        lines.append(f"{indent}    {k}: {_format_str_value(v, depth + 1)}")
    lines.append(f"{indent}}}")
    return '\n'.join(lines)

  
def stylish(diff: list, depth: int = 1) -> str:
    indent = ' ' * (depth * 4 - 2)
    lines = ['{']

    for node in diff:
        key = node['key']
        node_type = node['type']

        match node_type:
            case 'nested':
                children = stylish(node['children'], depth + 1)
                lines.append(f"{indent}  {key}: {children}")

            case 'added':
                value = _format_str_value(node['value'], depth)
                lines.append(f"{indent}+ {key}: {value}")

            case 'removed':
                value = _format_str_value(node['value'], depth)
                lines.append(f"{indent}- {key}: {value}")

            case 'unchanged':
                value = _format_str_value(node['value'], depth)
                lines.append(f"{indent}  {key}: {value}")

            case 'changed':
                old = _format_str_value(node['old_value'], depth)
                new = _format_str_value(node['new_value'], depth)
                lines.append(f"{indent}- {key}: {old}")
                lines.append(f"{indent}+ {key}: {new}")

    lines.append(' ' * ((depth - 1) * 4) + '}')
    return '\n'.join(lines)
    