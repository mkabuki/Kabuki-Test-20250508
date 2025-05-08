#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
鶴亀算を解くPythonスクリプト
鶴と亀の頭数と足の総数から、それぞれの匹数を求めます。
"""

def solve_tsurukame(heads, legs):
    """
    鶴亀算を解く関数
    
    Parameters:
    heads (int): 頭の総数
    legs (int): 足の総数
    
    Returns:
    tuple: (鶴の数, 亀の数) のタプル、または解が存在しない場合はNone
    """
    # 鶴は2本足、亀は4本足
    # 連立方程式:
    # x + y = heads (頭の数の合計)
    # 2x + 4y = legs (足の数の合計)
    
    # 解く:
    # x = heads - y
    # 2(heads - y) + 4y = legs
    # 2*heads - 2y + 4y = legs
    # 2*heads + 2y = legs
    # y = (legs - 2*heads) / 2
    
    tsuru = 0  # 鶴の数
    kame = 0   # 亀の数
    
    # 亀の数を計算
    kame = (legs - 2 * heads) / 2
    
    # 整数解かどうか確認
    if kame != int(kame) or kame < 0:
        return None
    
    kame = int(kame)
    tsuru = heads - kame
    
    # 鶴の数が負にならないか確認
    if tsuru < 0:
        return None
    
    return (tsuru, kame)

def main():
    """メイン関数: ユーザー入力を受け取り結果を表示"""
    print("=== 鶴亀算を解くプログラム ===")
    
    try:
        heads = int(input("頭の総数を入力してください: "))
        legs = int(input("足の総数を入力してください: "))
        
        if heads < 0 or legs < 0:
            print("頭と足の数は正の整数で入力してください。")
            return
        
        result = solve_tsurukame(heads, legs)
        
        if result is None:
            print("解が存在しません。入力を確認してください。")
        else:
            tsuru, kame = result
            print(f"鶴の数: {tsuru}羽")
            print(f"亀の数: {kame}匹")
            
            # 検算
            total_heads = tsuru + kame
            total_legs = 2 * tsuru + 4 * kame
            print(f"\n【検算】")
            print(f"頭の総数: {total_heads}")
            print(f"足の総数: {total_legs}")
    
    except ValueError:
        print("整数を入力してください。")

if __name__ == "__main__":
    main()

# 使用例：
# 頭の総数を入力してください: 8
# 足の総数を入力してください: 22
# 鶴の数: 5羽
# 亀の数: 3匹
#
# 【検算】
# 頭の総数: 8
# 足の総数: 22
