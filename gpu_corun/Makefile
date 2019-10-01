default: *.tex all.bib 
	pdflatex main
all: *.tex all.bib 
	pdflatex main
	bibtex main
	pdflatex main
	pdflatex main
	pdflatex main

clean:
	-@rm -f *~ *.bak *.out *.aux  *.bbl  *.blg  *.dvi  *.log  *.pdf
