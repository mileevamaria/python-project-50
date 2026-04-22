def format_value(value, depth):  # noqa: C901
    indent = ' ' * (depth * 4)
    if not isinstance(value, dict):
        return str(value)
    
    lines = ['{']
    for k, v in value.items():
        lines.append(f"{indent}    {k}: {format_value(v, depth + 1)}")
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
                value = format_value(node['value'], depth)
                lines.append(f"{indent}+ {key}: {value}")

            case 'removed':
                value = format_value(node['value'], depth)
                lines.append(f"{indent}- {key}: {value}")

            case 'unchanged':
                value = format_value(node['value'], depth)
                lines.append(f"{indent}  {key}: {value}")

            case 'changed':
                old = format_value(node['old_value'], depth)
                new = format_value(node['new_value'], depth)
                lines.append(f"{indent}- {key}: {old}")
                lines.append(f"{indent}+ {key}: {new}")

    lines.append(' ' * ((depth - 1) * 4) + '}')
    return '\n'.join(lines)
    