def simple_generator():
    yield "Hello"
    yield "World"
    yield "!"
    return simple_generator


# 创建一个生成器对象
gen = simple_generator

for batch_id, data in enumerate(gen()):
    print(batch_id, data)
