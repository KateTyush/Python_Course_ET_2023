import os
import re
import sys
import json
import datetime


def analyze_log_file(file_path):
    pattern = r'(\d+\.\d+\.\d+\.\d+) - - \[.*\] "(\w+) .+ HTTP/\d\.\d" \d+ \d+ ".+" ".+" (\d+)'
    regex = re.compile(pattern)

    total_requests = 0
    method_counts = {}
    ip_counts = {}
    longest_requests = []

    with open(file_path, "r") as file:
        for line in file:
            match = regex.search(line)
            if match:
                ip, method, duration = match.groups()
                total_requests += 1
                method_counts[method] = method_counts.get(method, 0) + 1
                ip_counts[ip] = ip_counts.get(ip, 0) + 1
                longest_requests.append(
                    {
                        "duration": int(duration),
                        "method": method,
                        "ip": ip,
                        "log_line": line.strip(),
                    }
                )

    longest_requests.sort(key=lambda x: x["duration"], reverse=True)
    longest_requests = longest_requests[:3]

    top_3_ips = sorted(ip_counts.items(), reverse=True)[:3]
    top_3_ips = [{"ip": ip, "count": count} for ip, count in top_3_ips]

    return {
        "total_requests": total_requests,
        "method_counts": method_counts,
        "top_3_ips": top_3_ips,
        "top_3_longest_requests": longest_requests,
    }


def analyze_logs_in_directory(directory_path):
    results = {}

    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".log"):
                file_path = os.path.join(root, file)
                results[file] = analyze_log_file(file_path)

    return results


def make_report(report):
    with open(datetime.datetime.now().strftime("%d-%m-%Y-%H:%M-log-analysis.json"), "w") as f:
        f.write(json.dumps(report, indent=4))

    print(json.dumps(report, indent=4))


def main():
    if len(sys.argv) < 2:
        print("Please specify the file path in the command line")
        return

    path = sys.argv[1]

    if not os.path.exists(path):
        print(f"This path {path} doesn't exist")
        return
    elif os.path.isdir(path):
        result = analyze_logs_in_directory(path)
        make_report(result)
    elif os.path.isfile(path):
        result = analyze_log_file(path)
        make_report(result)
    else:
        print(f"Something wrong")


if __name__ == "__main__":
    main()
