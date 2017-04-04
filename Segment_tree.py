__author__ = 'ratnesh.mishra'

tree = [0]*500000


def create_tree(node, start, last, state):
    if start == last:
        tree[node] = arr[start]
        create_tree.turn = 1
        return
    l = node << 1
    mid = (start+last) >> 1
    create_tree(l, start, mid, not state)
    create_tree(l+1, mid+1, last, not state)
    tree[node] = tree[l] | tree[l+1] if state else tree[l] ^ tree[l+1]


def update_tree(node, start, end, idx, state):
    if idx > end or idx < start:
        return
    if start == end:
        tree[node] = arr[start]
        return
    mid = (start + end) >> 1
    l = node << 1
    if mid >= idx:
        update_tree(l, start, mid, idx, not state)
    else:
        update_tree(l+1, mid+1, end, idx, not state)
    tree[node] = tree[l] | tree[l+1] if state else tree[l] ^ tree[l+1]


if __name__ == '__main__':
    try:
        n, m = map(int, input().split())
        arr = [0]
        p = 1 << n
        arr.extend(list(map(int, input().split())))
        create_tree(1, 1, p, n&1)
        for _ in range(m):
            i, val = map(int, input().split())
            if arr[i] != val:
                arr[i] = val
                update_tree(1, 1, p, i, n&1)
            print(tree[1])
    except Exception as e:
        print(str(e))




