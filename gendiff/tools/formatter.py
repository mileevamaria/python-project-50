class Formatter:
    @staticmethod
    def stylish(diff: dict) -> str:
        result = '{\n'
        for key in diff:
            match diff[key]['status']:
                case 'same':
                    result += f'    {key}: {diff[key]['data1']}\n'
                case 'removed':
                    result += f'  - {key}: {diff[key]['data1']}\n'
                case 'added':
                    result += f'  + {key}: {diff[key]['data2']}\n'
                case 'changed':
                    result += f'  - {key}: {diff[key]['data1']}\n'
                    result += f'  + {key}: {diff[key]['data2']}\n'
        result += '}'
        return result
        