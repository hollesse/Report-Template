#!/usr/bin/env sh

replaceUmlaute(){
  sed -i -- 's;Ã¶;\{\\\"o\};g' $1*.$2 # ö
  sed -i -- 's;Ã–;\{\\\"O\};g' $1*.$2 # Ö
  sed -i -- 's;Ã¤;\{\\\"a\};g' $1*.$2 # ä
  sed -i -- 's;Ã„;\{\\\"A\};g' $1*.$2 # Ä
  sed -i -- 's;Ã¼;\{\\\"u\};g' $1*.$2 # ü
  sed -i -- 's;Ãœ;\{\\\"U\};g' $1*.$2 # Ü
  sed -i -- 's;ÃŸ;\{\\ss\};g' $1*.$2 # ß
}


replaceUmlauteTex() {
    replaceUmlaute $1 tex
}

replaceUmlauteBib() {
    replaceUmlaute $1 bib
}

replaceUmlauteTex template/
replaceUmlauteTex userdata/
replaceUmlauteTex userdata/lib/listing/
replaceUmlauteTex userdata/ExampleContent/content/
replaceUmlauteTex userdata/ExampleContent/content/chapters/
replaceUmlauteBib userdata/ExampleContent/resources/
