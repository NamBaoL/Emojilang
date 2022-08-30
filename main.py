file = open("run.txt", encoding='utf-8')
code = "⬜⬛❓◾◽➡⬆⬇▶❌➕✖➗➿➰⬅♾♊〰⚪🔢🔡🔤🔠🆎⏳".replace(u"\ufe0f", "")
compile = "import time\nimport math\nimport random\nans = ''\nstack = []\n"
ans = ""
stack = []
tabs = 0
loop = 'abcdefghijklmnopqrstuvwxyz'
ir = 0


def text(data, x=1):
    global compile, tabs
    compile += "\t" * tabs
    compile += data + ('\n' * x)


def compiler(data):
    global ans, stack, compile, tabs, code, loop, ir
    for j in data:
        if j == code[0]:
            text("print(ans)")
        elif j == code[1]:
            text("print(ans, end='')")
        elif j == code[2]:
            text("ans = input()")
        elif j == code[3]:
            pass
        elif j == code[4]:
            text("ans = stack[int(ans)]")
            ans = stack[int(ans)]
        elif j == code[5]:
            if ans == "-1":
                text("if float(stack[-2])<float(stack[-1]):")
            elif ans == "1":
                text("if float(stack[-2])>float(stack[-1]):")
            elif ans == "0":
                text("if float(stack[-2])==float(stack[-1]):")
            elif ans == "-2":
                text("if float(stack[-2])<=float(stack[-1]):")
            elif ans == "2":
                text("if float(stack[-2])>=float(stack[-1]):")
            tabs += 1
        elif j == code[6]:
            text("stack.append(ans)")
            stack.append(ans)
        elif j == code[7]:
            text("ans = stack[-1]")
            ans = stack[-1]
        elif j == code[8]:
            tabs -= 1
        elif j == code[9]:
            text('ans = ""')
            ans = ''
        elif j == code[10]:
            text('stack[-2] = float(stack[-2])+float(stack[-1])')
            text('del stack[-1]')
        elif j == code[11]:
            text('stack[-2] = float(stack[-2])*float(stack[-1])')
            text('del stack[-1]')
        elif j == code[12]:
            text('stack[-2] = float(stack[-2])/float(stack[-1])')
            text('del stack[-1]')
        elif j == code[13]:
            if ans == "-1":
                text("while float(stack[-2])<float(stack[-1]):")
            elif ans == "1":
                text("while float(stack[-2])>float(stack[-1]):")
            elif ans == "0":
                text("while float(stack[-2])==float(stack[-1]):")
            elif ans == "-2":
                text("while float(stack[-2])<=float(stack[-1]):")
            elif ans == "2":
                text("while float(stack[-2])>=float(stack[-1]):")
            tabs += 1
        elif j == code[14]:
            text(f'for {loop[ir]} in range(float(ans)):')
            ir += 1
            tabs += 1
        elif j == code[15]:
            text('else:')
            tabs += 1
        elif j == code[16]:
            text('ans = random.randint(0, int(ans))')
        elif j == code[17]:
            text('ans = math.pi')
        elif j == code[18]:
            text('ans = math.sin(float(ans))')
        elif j == code[19]:
            text('ans = math.radians(float(ans))')
        elif j == code[20]:
            text('ans = int(ans)')
        elif j == code[21]:
            if ans == "-1":
                text("if stack[-2]<stack[-1]:")
            elif ans == "1":
                text("if stack[-2]>stack[-1]:")
            elif ans == "0":
                text("if stack[-2]==stack[-1]:")
            elif ans == "-2":
                text("if stack[-2]<=stack[-1]:")
            elif ans == "2":
                text("if stack[-2]>=stack[-1]:")
            elif ans == "3":
                text("if stack[-2] in stack[-1]:")
            tabs += 1
        elif j == code[22]:
            text('ans = ans.lower()')
        elif j == code[23]:
            text('ans = ans.upper()')
        elif j == code[24]:
            if ans == "-1":
                text("while stack[-2]<stack[-1]:")
            elif ans == "1":
                text("while stack[-2]>stack[-1]:")
            elif ans == "0":
                text("while stack[-2]==stack[-1]:")
            elif ans == "-2":
                text("while stack[-2]<=stack[-1]:")
            elif ans == "2":
                text("while stack[-2]>=stack[-1]:")
            elif ans == "3":
                text("while stack[-2] in stack[-1]:")
            tabs += 1
        elif j == code[25]:
            text('time.sleep(float(ans))')
        else:
            text(f"ans += '{j}'")
            ans += j


for i in file.readlines():
    compiler(i.replace(u"\ufe0f", ""))
print(compile)
exec(compile)
# print(stack)
