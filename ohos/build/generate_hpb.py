#!/usr/bin/env python3
# coding: utf-8
# Copyright (c) 2024 Huawei Device Co., Ltd.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import sys
import subprocess

def main():
    if len(sys.argv) != 4:
        print("Usage: python generate_hpb.py <hpb_transform_exe> <input_tex_file> <output_hpb_file>")
        sys.exit(1)

    hpb_transform_exe = sys.argv[1]
    input_tex_file = sys.argv[2]
    output_hpb_file = sys.argv[3]

    # 构建命令
    command = f"{hpb_transform_exe} {input_tex_file} {output_hpb_file}"
    print(f"hpy_command: {command}")

    # 执行命令
    # result = subprocess.run(command, shell=True)
    # if result.returncode != 0:
    #     print(f"Error: Command '{command}' failed with return code {result.returncode}")
    #     sys.exit(1)

if __name__ == "__main__":
    main()
