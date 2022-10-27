
import tempfile


class DataFilesManager:

    def read_line_for_value(self, str_to_find, pos, file_path):

        with open(file_path, mode='r') as txt_file:
            for line in txt_file:
                temp = (line.strip()).split()
                if line and str_to_find == temp[pos]:
                    content = line.strip()
                    return content
        
        raise ValueError('No such content in file')

    def write_line(self, content, file_path):

        with open(file_path, 'a') as txt_file:
            txt_file.write(content + '\n')

    def update_line(self, content, str_check, pos, file_path):
        
        with tempfile.TemporaryFile(mode='w+t') as fp:
            with open(file_path, mode='r') as txt_file:
                for line in txt_file:
                    temp = line.strip()
                    if str_check == temp[pos]:
                        fp.write(content + '\n')
                    else:
                        fp.write(temp + '\n')
            fp.seek(0)
            with open(file_path, mode='w') as txt_file:
                
                temp_line = fp.read()
                txt_file.write(temp_line)

    def remove_line(self, line, file_path):
        file_content = self.read_file(file_path)
        
        if line in file_content:
            file_content.remove(line)
        else:
            raise ValueError('No such content in file')

        with open(file_path, mode='w') as txt_file:
            txt_file.write('\n'.join(file_content) + '\n')
            # txt_file.write('\n')

        return 'removed successfully'

    def read_file(self, file_path) -> list[str]:

        with open(file_path, mode='r') as txt_file:
            lines = []
            for line in txt_file:
                lines.append(line.strip('\n'))
        if not lines:
            raise ValueError('File is empty')
        return lines

    def create_file(self, file_path):
        f = open(file_path, mode='w')
        f.close()
        