import { readFileSync } from "fs";
import * as path from 'path';

const load_data = (file_path: string): string => {
    console.log(path.resolve(__dirname))
    const data = readFileSync(path.resolve(file_path), 'utf-8');
    console.log(data)
    return data;
}

load_data("./input.txt")