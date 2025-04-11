def add_prefix_to_file(input_file, output_file, prefix="{墨茶}"):
    """
    将指定前缀添加到文本文件的每一行开头
    
    参数:
    input_file (str): 输入文件的路径
    output_file (str): 输出文件的路径
    prefix (str): 要添加的前缀，默认为 "{墨茶}"
    """
    try:
        # 读取输入文件
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # 添加前缀并写入输出文件
        with open(output_file, 'w', encoding='utf-8') as f:
            for line in lines:
                f.write(f"{prefix}{line}")
        
        print(f"处理完成！已将前缀 '{prefix}' 添加到 {len(lines)} 行文本，并保存到 {output_file}")
        
    except Exception as e:
        print(f"发生错误: {e}")

# 使用示例
if __name__ == "__main__":
    input_file = "rip.txt"  # 输入文件路径
    output_file = "rip_with_prefix.txt"  # 输出文件路径
    add_prefix_to_file(input_file, output_file)