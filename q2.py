letter = '''
            Dear <|Name|> ,
            Yau are Selected |
            <|Date|>
            '''
print(letter.replace("<|Name|>", "King").replace("<|Date|>","26"))
