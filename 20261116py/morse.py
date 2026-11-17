class Name:
    def __init__(self, ,문자, 신호):
        self.writing = 문자
        self.mor = 신호
        
        for i in 신호:
            if i == '.' :
                flash.value(1)
                time.sleep(0.2)
                flash.value(0)
                time.sleep(0.2)
            elif o == '-':
                flash.value(1)
                time.sleep(0.6)
                flash.value(0)
                time.sleep(0.2)