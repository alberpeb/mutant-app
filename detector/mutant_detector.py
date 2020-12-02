class MutantDetector:
    '''
    This class is in charge of iterating over a DNA 
    sample (as an array) and finding patterns. 
    When hitting more than one pattern, the check() 
    method will return True, otherwise False.
    For example:

    >> md = MutantDetector (array);
    >> md.check ()
    True
    '''
    PATTERN_LENGTH = 4
    BLOCKED = "*"
    patterns = [str(PATTERN_LENGTH*"A"),
                    str(PATTERN_LENGTH*"T"),
                    str(PATTERN_LENGTH*"C"),
                    str(PATTERN_LENGTH*"G")]
    
    def __init__(self, array):
        self.array = array
        self.rows = len(array)
        self.cols = len(array[0])
        #Counting the number of matches with a pattern
        self.total_matches = 0
   
    def check(self):
        '''
        In this method, the provided array is traversed in 
        all directions where each sequence of characters is 
        evaluated with the possible patterns
        '''
        self.iterate_horizontal()
        if self.is_mutant():
            return True
        self.iterate_vertical()
        if self.is_mutant():
            return True
        self.iterate_diagonals()
        if self.is_mutant():
            return True
        self.iterate_diagonals_inv()
        return self.is_mutant()

    def is_mutant(self):
        return self.total_matches > 1

    def iterate_horizontal(self):
        for index in range(len(self.array)):
            for pattern in self.patterns:
                while True:
                    ''' Every iteration in every direction
                    may have more than one pattern coincidence
                    '''
                    pos = self.array[index].find(pattern)
                    if pos != -1:
                        self.block_horizontal(index, pos)
                        self.total_matches += 1
                        if self.is_mutant():
                            return
                    else:
                        break

    def block_horizontal(self, index, pos):
        for cell in range(self.PATTERN_LENGTH):
            row_as_list = list(self.array[index])
            row_as_list[pos + cell] = self.BLOCKED
            self.array[index] = "".join(row_as_list)

    def iterate_vertical(self):
        for col in range(self.rows):
            while True:
                sequence = ""
                for row in self.array:
                    sequence += row[col]
                self.check_vertical_pattern(sequence, col)
                if self.is_mutant():
                    return
                else:
                    break
        
    def check_vertical_pattern(self, sequence, col):
        for pattern in self.patterns:
            pos = sequence.find(pattern)
            if pos != -1 and self.not_blocked_vertical(col, pos):
                self.block_vertical(col, pos)
                self.total_matches +=1

    def not_blocked_vertical(self, col, pos):
        for row in range(self.PATTERN_LENGTH):
            lst_row = list(self.array[row + pos])
            if lst_row[col] == self.BLOCKED:
                return False
        return True
        

    def block_vertical(self, col, row_pos):
        for row in range(self.PATTERN_LENGTH):
            lst_row = list(self.array[row + row_pos])
            lst_row[col] = self.BLOCKED
            self.array[row + row_pos] = "".join(lst_row)

    def iterate_diagonals(self):
        ##Every diagonal iteration may have a number of
        ## "diagonal rows". Check the sentence below:
        diagonal_rows = self.rows + self.cols - 1
        for diag in range(diagonal_rows):
            while True:
                sequence = ""
                for val in range(diag + 1):
                    i = diag - val
                    if(i < self.rows and val < self.cols):
                        sequence += self.array[i][val]
                if len(sequence) >= self.PATTERN_LENGTH:
                    self.match_sequence(sequence, diag)
                if self.is_mutant():
                    return
                else:
                    break

    def match_sequence(self, sequence, diag):
        for pattern in self.patterns:
            pos = sequence.find(pattern)
            if pos != -1 and self.not_blocked_diagonal(pos, diag):
                self.block_pos_diagonal(pos, diag)
                self.total_matches += 1
                if self.is_mutant():
                    return

    def not_blocked_diagonal(self, pos, diag):
        '''
            By the index of diagonal 'diag' and the position 'pos' where this traversional pattern start, the pattern
            must be checked by it's entire lenght. Every iteration will check from bottom left to up right in the diagonal direction
        '''
        for pattern_len in range(self.PATTERN_LENGTH):
            #i = diag - pattern_len
            if diag <= ((self.rows + self.cols) // 2):
                row = diag - pos - pattern_len
                col = pos + pattern_len
            else:
                row = self.rows - 1 - pattern_len
                col = (self.rows + self.cols) - diag + pos + pattern_len
            if(row < self.rows and col < self.cols):
                if self.array[row][col] == self.BLOCKED:
                    return False
        return True

    def block_pos_diagonal(self, pos, diag):
        for pattern_len in range(self.PATTERN_LENGTH):
            #i = diag - pattern_len
            if diag < ((self.rows + self.cols) // 2):
                row = diag - pos - pattern_len
                col = pos + pattern_len
            else:
                row = self.rows - 1 - pos - pattern_len
                col = diag - (self.rows - 1) + pos + pattern_len
            if(row < self.rows and col < self.cols):
                row_as_list = list(self.array[row])
                row_as_list[col] = self.BLOCKED
                self.array[row] = "".join(row_as_list)

    def iterate_diagonals_inv(self):
        row = self.rows
        for diag in range(self.rows + self.cols - 1):
            while True:
                sequence = ""
                row -= 1
                for y, x in zip(range(row, self.rows), range(self.rows)):
                    if y < 0:
                        continue
                    sequence += self.array[y][x]
                if len(sequence) >= self.PATTERN_LENGTH:
                    rest = 1 if diag < (self.rows + self.cols) // 2 else 0
                    self.match_sequence_inv(sequence, (row, self.rows), rest)
                if self.is_mutant():
                    return
                else:
                    break

    def match_sequence_inv(self, sequence, diag, rest):
        for pattern in self.patterns:
                pos = sequence.find(pattern)
                if pos != -1 and self.not_blocked_diagonal_inv(pos, diag, rest):
                    self.block_pos_diagonal_inv(pos, diag, rest)
                    self.total_matches += 1
                    if self.is_mutant():
                        return

    def not_blocked_diagonal_inv(self, pos, diag, rest):
        pos_count = 0
        pos -= rest
        for y, x in zip(range(diag[0], diag[1]), range(diag[1])):
            if pos_count > pos and pos_count <= (pos + self.PATTERN_LENGTH):
                if self.array[y][x] == self.BLOCKED:
                    return False
            pos_count += 1
        return True

    def block_pos_diagonal_inv(self, pos, diag, rest):
        pos_count = 0
        pos -= rest
        for y, x in zip(range(diag[0], diag[1]), range(diag[1])):
            if pos_count > pos and pos_count <= (pos + self.PATTERN_LENGTH):
                row_as_list = list(self.array[y])
                row_as_list[x] = self.BLOCKED
                self.array[y] = "".join(row_as_list)
            pos_count += 1

def is_mutant(array) -> bool:
    '''
    Main function in charge of instantiating the 
    Detector, looking for patterns and returning 
    the result
    '''
    p = MutantDetector(array)
    return p.check()