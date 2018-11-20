class tree():
    def __init__(self,data):
        self.data = data

    def to_tree(self,pid_id='0', level=0, html='┗━━━'):
        items = self.data

        tree_list = []
        for item in items:
            if str(item['pid_id']) == str(pid_id):
                item['level'] = int(level) + 1
                item['html'] = html * int(level)
                tree_list.append(item)
                tree_list = tree_list + self.to_tree(pid_id=item['id'], level=level + 1, html='┗━━━')
        return tree_list

    def to_tree_ul(self):
        list = self.data
        def tree(items=[], pid_id='0'):
            tree_list = []
            html = ''
            for item in items:
                if str(item['parent_id']).replace('-', '') == pid_id:
                    html += '<ul class="col-sm-2">'
                    html += '<li><a href="'+item['url']+'">'+item['name']+'</a></li>'
                    tree_list = tree_list + tree(items, pid_id=item['id'])
                    html += '</ul>'
                else:
                    html += '<li><a href="'+item['url']+'">'+item['name']+'</a></li>'
            return tree_list

        result = tree(list, pid_id=0)
        return result

    #获取某个导航下面的子导航
    def get_childs(self,pid_id='0'):
        pid_id = str(pid_id)
        items = self.data
        dic = {}
        dic[pid_id] = []
        for item in items:
            dic[str(item['pid_id'])] = []
        for item in items:
            dic[str(item['pid_id'])].append(item)

        return dic[pid_id]

    #实现无限极分类导航
    def to_be_tree(self,pid_id='0'):
        items = self.get_childs(pid_id)
        def to_tree(items=[]):
            list_list = []
            for item in items:
                id = str(item['id']).replace('-','')
                childs = self.get_childs(id)
                if len(childs)>=1:
                    item['children'] = to_tree(childs)
                else:
                    item['children'] = childs
                list_list.append(item)
            return list_list
        return to_tree(items)