import re


class StatementType:
    USE = re.compile(r"Use \w+")
    DEFINE = re.compile(r"Def \w+ : \w+")
    FINISH = re.compile(r"End")
    SUBPROP = re.compile(r"\w+\.\w+:")
    PROP = re.compile(r"\w+:")


class OperationType:
    Use = 0
    Define = 1
    Finish = 2
    SetProperty = 3
    SetSubProperty = 4


class Parser:
    def __init__(self):
        self.parsed_lines = []

    def parse(self, file: str):
        with open(file) as file:
            for idx, line in enumerate(file.readlines()):
                line = line.strip()
                if line == "" or line.startswith("#"):
                    continue
                elif StatementType.DEFINE.match(line):
                    self.parse_define(line)
                elif StatementType.FINISH.match(line):
                    self.parse_finish(line)
                elif StatementType.PROP.match(line):
                    self.parse_prop(line)
                elif StatementType.SUBPROP.match(line):
                    self.parse_subprop(line)
                elif StatementType.USE.match(line):
                    self.parse_use(line)
                else:
                    raise Exception(f"Invalid statement: '{line}' at line {idx + 1}")

    @staticmethod
    def split_line(string):
        result = []
        idx = 0
        str_start = None
        look_for_spaces = True
        start_idx = 0

        for char in string:
            if char == " " and look_for_spaces:
                result.append(string[start_idx:idx])
                start_idx = idx + 1
            elif char == "#" and look_for_spaces:
                break
            elif char == '"':
                look_for_spaces = False
                if str_start is None:
                    str_start = idx + 1
                else:
                    str_end = idx
                    result.append(string[str_start:str_end])
                    start_idx = idx + 2
                    look_for_spaces = True
                    str_start = None

            if idx == len(string) - 1:
                result.append(string[start_idx:])

            idx += 1
        return [token for token in result if token != ""]

    def parse_define(self, line):
        line = line.replace(" ", "").replace("Def", "")
        line = line.split(":")
        line.insert(0, OperationType.Define)
        self.parsed_lines.append(line)

    def parse_finish(self, line):
        line = line.replace("End", "").split()
        line.insert(0, OperationType.Finish)
        self.parsed_lines.append(line)

    def parse_use(self, line):
        line = line.replace("Use", "").split()
        line.insert(0, OperationType.Use)
        self.parsed_lines.append(line)

    def parse_prop(self, line):
        line = line.split(":", 1)
        value = self.split_line(line[1])
        del line[1]
        line.extend(value)
        line.insert(0, OperationType.SetProperty)
        self.parsed_lines.append(line)

    def parse_subprop(self, line):
        line = line.replace(" ", "")
        line = line.replace('"', '')
        line = line.split(":")
        properties = line[0].split(".")
        del line[0]
        line.extend(properties)
        line.insert(0, OperationType.SetSubProperty)
        self.parsed_lines.append(line)
