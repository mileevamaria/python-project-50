def _format_plain_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, str):
        return f'\'{value}\''
    elif value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    return str(value)


def plain(diff: list, parent_path: str = '') -> str:
    lines = []
    for node in diff:
        key = node['key']
        node_type = node['type']
        path = f'{parent_path}.{key}' if parent_path else key

        match node_type:
            case 'nested':
                lines.append(plain(node['children'], path))
            case 'added':
                value = _format_plain_value(node['value'])
                lines.append(
                    f'Property \'{path}\' was added with value: {value}')
            case 'removed':
                lines.append(f'Property \'{path}\' was removed')
            case 'changed':
                old = _format_plain_value(node['old_value'])
                new = _format_plain_value(node['new_value'])
                lines.append(
                    f'Property \'{path}\' was updated. From {old} to {new}'
                )

    return '\n'.join(lines)
