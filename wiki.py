import  wikipedia


wikipedia.set_lang("pt")

assunto = wikipedia.search(input("Assunto da wiki:"))
print(assunto)
print("...")
pagina = wikipedia.page(assunto[0])
print("Conteudo Completo:"); completo = pagina.content; print(completo)
print("*#*" * 30)
print("Conteudo Completo:"); resumido = pagina.summary; print(resumido)
