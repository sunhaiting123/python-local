user_tags = dict()
tag_items = dict()
user_items = dict()


# def InitStat(records):
# for user, item, tag in records.items():
# addValueToMat(user_tags, user, tag, 1)
# addValueToMat(tag_items, tag, item, 1)
# addValueToMat(user_items, user, item, 1)


def Recommend(user):
    recommend_items = dict()
    tagged_items = user_items[user]
    for tag, wut in user_tags[user].items():
        for item, wti in tag_items[tag].items():
            if item in tagged_items:
                continue
            if item not in recommend_items:
                recommend_items[item] = wut * wti
            else:
                recommend_items[item] += wut * wti
    return recommend_items
