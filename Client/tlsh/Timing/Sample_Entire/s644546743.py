def main():
    cross_sections = input()
    s1 = []
    s2 = []
    total_surface = 0
    for i, cross_section in enumerate(cross_sections):
        if cross_section == '\\':
            s1.append(i)
        elif cross_section == '/' and s1:
            ip = s1.pop()
            # calc total surface
            sub_surface = i - ip
            total_surface += sub_surface
            # calc sub surface
            for s in reversed(s2):
                if s[0] > ip:
                    sub_surface += s2.pop()[1]
                else:
                    break
            s2.append((ip, sub_surface))

    print(total_surface)
    if s2:
        print(len(s2), ' '.join(map(lambda x: str(x[1]), s2)))
    else:
        print(len(s2))


if __name__ == "__main__":
    main()

