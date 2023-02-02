sakinys = "The Zen of Python"
#naujas_sakinys = map(str, sakinys.split())
naujas_sakinys_saukt = map(lambda zenklas: zenklas + "!", sakinys.split())
#print(list(naujas_sakinys_saukt))
print(" ".join(naujas_sakinys_saukt))