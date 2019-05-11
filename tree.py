
# -*- coding: utf-8 -*-

import os, sys

# 原作者：Freeman耀
# 网址：https://www.cnblogs.com/freeman818/p/7252041.html
# 修改内容：增加打印图形化二叉树功能
# 作者：张燕飞
# 时间：2019年5月11日


class Node:
    tree_depth = -1

    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left    # 左子树
        self.right = right  # 右子树

    def preTraverse(self, current_node):
        '''
        前序遍历
        '''
        if current_node == None:
            return

        print(str(current_node.value), end=' ')
        self.preTraverse(current_node.left)
        self.preTraverse(current_node.right)

    def midTraverse(self, current_node):
        '''
        中序遍历
        '''
        if current_node == None:
            return

        self.midTraverse(current_node.left)
        print(str(current_node.value), end=' ')
        self.midTraverse(current_node.right)

    def afterTraverse(self, current_node):
        '''
        后序遍历
        '''
        if current_node == None:
            return

        self.afterTraverse(current_node.left)
        self.afterTraverse(current_node.right)
        print(str(current_node.value), end=' ')

    def fill_graph(self, graph, parents):
        line = []
        children = []
        null_count = 0
        for node in parents:
            if node is None:
                line.append('.')
                null_count = null_count + 1
                children.append(None)
                children.append(None)
            else:
                line.append(node.value)
                children.append(node.left)
                children.append(node.right)

        if len(children) == (null_count * 2):
            return

        graph.append(line)
        self.fill_graph(graph, children)

    def graph_show(self, root_node):
        node_lines = []
        self.fill_graph(node_lines, [root_node])
        line_count = len(node_lines)
        tree_graph = []
        for i in range(0, line_count - 1):
            prev_line2 = ''
            prev_line1 = ''
            this_line = ''
            left = None
            for value in node_lines[i]:
                this_line += ' ' * (pow(2, line_count - i) - 1) + value + ' ' * pow(2, line_count - i)
                if i == 0:
                    continue
                if left is None:
                    left = value
                    continue

                if left == ' ' and value == ' ':
                    prev_line2 += ' ' * pow(2, line_count - i + 2)
                    prev_line1 += ' ' * pow(2, line_count - i + 2)

                if left != ' ' and value == ' ':
                    prev_line2 += ' ' * (pow(2, line_count - i + 1) - 1) + '/' + ' ' * pow(2, line_count - i + 1)
                    prev_line1 += ' ' * pow(2, line_count - i) + '/' + '-' * (pow(2, line_count - i) - 2) + ' ' * (
                                pow(2, line_count - i) + 1)

                if left != ' ' and value != ' ':
                    prev_line2 += ' ' * (pow(2, line_count - i + 1) - 1) + '|' + ' ' * pow(2, line_count - i + 1)
                    prev_line1 += ' ' * pow(2, line_count - i) + '/' + '-' * (
                                pow(2, line_count - i + 1) - 3) + '\\' + ' ' * (pow(2, line_count - i) + 1)

                if left == ' ' and value != ' ':
                    prev_line2 += ' ' * (pow(2, line_count - i + 1) - 1) + '\\' + ' ' * pow(2, line_count - i + 1)
                    prev_line1 += ' ' * pow(2, line_count - i + 1) + '-' * (pow(2, line_count - i) - 2) + '\\' + ' ' * (
                                pow(2, line_count - i + 1) + 1)

                left = None
            if i == 0:
                tree_graph.append(this_line)
                continue

            tree_graph.append(prev_line2)
            tree_graph.append(prev_line1)
            tree_graph.append(this_line)


        for i in range(line_count - 1, line_count):
            prev_line1 = ''
            this_line = ''
            left = None
            for value in node_lines[i]:
                this_line += ' ' * (pow(2, line_count - i) - 1) + value + ' ' * pow(2, line_count - i)
                if i == 0:
                    continue
                if left is None:
                    left = value
                    continue

                if left == ' ' and value == ' ':
                    prev_line1 += ' ' * pow(2, line_count - i + 2)

                if left != ' ' and value == ' ':
                    prev_line1 += ' ' * pow(2, line_count - i) + '/' + ' ' * (pow(2, line_count - i) - 2) + ' ' * (
                                pow(2, line_count - i) + 1)

                if left != ' ' and value != ' ':
                    prev_line1 += ' ' * pow(2, line_count - i) + '/' + ' ' * (
                                pow(2, line_count - i + 1) - 3) + '\\' + ' ' * (pow(2, line_count - i) + 1)

                if left == ' ' and value != ' ':
                    prev_line1 += ' ' * pow(2, line_count - i + 1) + ' ' * (pow(2, line_count - i) - 2) + '\\' + ' ' * (
                                pow(2, line_count - i + 1) + 1)

                left = None

            tree_graph.append(prev_line1)
            tree_graph.append(this_line)

        print('-' * (len(tree_graph[2]) + 4))
        for line in tree_graph:
            print('|', line, '|')

        print('-' * (len(tree_graph[0]) + 4))
        return

if __name__ == '__main__':
    '''
           D
         /   \
        B     E
       / \     \
      A   C     G
               /
              F      
    '''
    root = Node('D', Node('B', Node('A'), Node('C')),Node('E', right=Node('G',Node('F'))))
    root.graph_show(root)

    print('前序遍历：', end='')
    root.preTraverse(root)
    print('\n中序遍历：', end='')
    root.midTraverse(root)
    print('\n后序遍历：', end='')
    root.afterTraverse(root)

