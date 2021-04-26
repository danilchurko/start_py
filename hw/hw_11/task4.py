def fake_string(string, pat, rem_pat, times):
    string = string.replace(pat, rem_pat, times)
    return print(string)


fake_string('DC makes good movies, DC makes good comics', 'DC', 'Marvel', 2)
