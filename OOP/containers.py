class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)

cloud = TagCloud()
cloud["hello"] = 10
cloud.add("hello")
len(cloud)
cloud.add("hello")
cloud.add("Hello")
cloud.add("hello")
cloud.add("Hello")

# print(cloud.__tags)