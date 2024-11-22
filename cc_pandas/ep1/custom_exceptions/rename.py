class UnknownColumnToRename(Exception):
    def __init__(self, column_name: str):
        super().__init__(f"UnknownColumnToRename for column: '{column_name}'")
