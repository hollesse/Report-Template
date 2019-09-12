# Internship Report Template for DHBW Mannheim Faculty Technology
This template is in development. It's based on [Luca Vazzano's template](https://github.com/LucaVazz/Report-Template) and it's customized for use at DB Systel (it does not correspond to the DB Cooperate Design).  

Please use XeLaTeX or LuaLaTex for building.
## Buildstatus
[![Build Status](https://travis-ci.org/hollesse/Report-Template.svg?branch=master)](https://travis-ci.org/hollesse/Report-Template)

## Features
- all formal layout-properties of the document are in accordance to the requirements given by the Technical Faculty of DHBW Mannheim.
- Titlepages for Internship Reports, Study Reports and Bachelor Thesis in accordance to these requirements included

<img alt="various Titlepages" src="http://i.imgur.com/ddOe000.png" width="70%">

- Fully customizable coloring

<img alt="Coloring" src="http://i.imgur.com/TGjZShi.png" width="70%">

- Easy switching between the (default) *english* and *german* version of the document



## How to Setup and Use
### Create New project
#### Either Run the project creation script (requires python 3.6 or higher)
`cd userdata`<br>
`python3 create_project.py`

Follow the instructions

#### Or do it the traditional way
1. Copy directory `./userdata/ExampleContent` to `./userdata/` and rename it. For example you can call it `PraxisT1000` if its your first internship report.<br>
`cp userdata/ExampleContent/* userdata/<project name>`
2. inside `./userdata/usersetup.tex`:
    - choose the type of your Report
	- choose your prefered Theme (DB Systel or DB default)
    - choose if you want to use the DB Font (have to be added by yourself - you can find instructions for that below)	
    - add the name of your content directory which we copied in step 1
    - choose if you want to write your report in english or german
    - fill out the fields for your informations

### Additional steps

3. place the entries for your bibliography into `./userdata/ <YOUR CONTENT DIRECTORY> /resources/references.bib`
4. place the `.tex`-files containing your content into `./userdata/ <YOUR CONTENT DIRECTORY> /content` and define the structure of your content inside `./userdata/ <YOUR CONTENT DIRECTORY> /content/content.tex`
5. fill your acronyms and custom macros as needed into `./userdata/ <YOUR CONTENT DIRECTORY> /content/acronyms.tex` and `./userdata/macros.tex`
6. save your image files into `./userdata/ <YOUR CONTENT DIRECTORY> /resources/images`
    - you can then use them easily by just referencing `\includegraphics{asdf}` if you saved your file at `./resources/images/asdf.png`

## How to use DB Fonts
The DB Fonts aren't included in this Repository, so you have to add them by yourself.
### Either run the installation script (automatically done by project creation script)
`cd userdata`
`python3 add_db_fonts.py`

Step 4 is omitted by the `add_db_fonts.py` script, but done by the `create_project.py`script.

### Or add the fonts manually
1. Create a new directory `./userdata/lib/fonts/db/`
2. Add the font DB Sans as Truetypefont in the Styles:
    - regular: `DB_Sans.ttf`
    - bold: `DB_Sans_Bold.tff`
    - italic: `DB_Sans_Italic.tff`
	- bold italic: `DB_Sans_Bold_Italic.tff`
2. Add the font DB Head as Truetypefont in the Styles:
    - regular: `DB_Head.ttf`
    - black: `DB_Head_Black.tff`
    - italic: `DB_Head_Italic.tff`
	- black italic: `DB_Head_Black_Italic.tff`
4. Activate DbFont in `./userdata/usersetup.tex` by removing the `%` Symbol in front of `DbFont` in the `usepackage` section


## Included Custom Elements for Ease of Use
**Note:** `<asdf>` inside the general code denotes a placeholder


#### striped Tables
```Latex
\begin{stripedacenttable}
    {<caption>}
    {\label{tab:<label>}}
    {<formating>}
    {<Headings-Content>}
    <row definitions>
\end{stripedacenttable}

\begin{stripedtable}
    {<caption>}
    {\label{tab:<label>}}
    {<coloring>}
    {<formating>}
    {<Headings-Content>}
    <row definitions>
\end{stripedtable}
```

- *<label>* needs to be enclosed inside `\label` to keep the auto-completion functionality of your editor working correctly
- formating should have the form `x^x^x^...` where `x` specifies the alignment for the column
    + possible aligments: `l`: left-aligned , `c`: centered , `r`: right-aligned

> *Example (with captions):*
> ```Latex
\begin{stripedacenttable}
    {A plain but nice looking table}
    {\label{tab:ex1}}
    {c^l^l}
    {Quarter & asdf & foobar}
    prev. Year & 42 & 17 \\
    Q1 & -3 & -7 \\
    Q2 & +7 & -1 \\
    Q3 & -4 & +12 \\
    Q4 & +2 & +2 \\
\end{stripedacenttable}

>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Ut purus elit, vestibulum ut, placerat ac, adipiscing vitae, felis.

>\begin{stripedtable}
    {A colorful, nice looking table}
    {\label{tab:ex1}}
    {Green}
    {c^l^l}
    {Quarter & asdf & foobar}
    prev. Year & 42 & 17 \\
    Q1 & -3 & -7 \\
    Q2 & +7 & -1 \\
    Q3 & -4 & +12 \\
    Q4 & +2 & +2 \\
\end{stripedtable}
```

> <img alt="Tables" src="http://i.imgur.com/8FzhRYr.png" width="65%">


#### Code Listings
```Latex
\begin{lstlisting}[
    caption={<description of your program>},
    label={lst:<label>},
    captionpos=b,
    language=<language-name>
]
<your code>
\end{lstlisting}
```

> *Example:*
> ```Latex
\begin{lstlisting}[
    caption={The Classic, realized in Python},
    label={lst:python1},
    captionpos=b,
    language=Python
]
> # classic
>
> hi = "Hello Wolrd"
print(hi)
\end{lstlisting}
```

> <img alt="Code Lisitng" src="http://i.imgur.com/8zXqzOZ.png" width="70%">


#### Fancy Symbols
The FontAwesome Package is bundeled into this repository, so you can use [all the nice symbols.](http://mirrors.ctan.org/fonts/fontawesome/doc/fontawesome.pdf).

> *Example:*
> ````Latex
> \faFileTextO{} \faStar{}\faStar{}\faStar{}\faStar{}\faStar{} $=$ \faGraduationCap{}
> ````

> <img alt="Code Lisitng" src="http://i.imgur.com/wZAVaom.png" width="14%">

The MarVoSym-Package is also loaded to provide [additional symbols](http://texdoc.net/texmf-dist/doc/fonts/marvosym/marvodoc.pdf).

> *Example:*
> ````Latex
> \Estatically{} \Forward{} \Printer{} \ \ \MVRightArrow{} \ \ \EyesDollar\EyesDollar\EyesDollar
> ````

> <img alt="Code Lisitng" src="http://i.imgur.com/lZ64aQA.png" width="14%">


#### Citations in the Footnotes
````Latex
\footnotecite{<source-reference>}
```


#### Mark Incomplete Things You Need To Do
````Latex
\incompletemarker{<note>}
```

> <img alt="Code Lisitng" src="http://i.imgur.com/eSQSoao.png" width="40%">


#### Prevent Pagebreaks absolutely, definitively
```Latex
\begin{absolutelynopagebreak}
    <content>
\end{absolutelynopagebreak}
```



---



## Contributing
I'm open for all forks, feedback and Pull Requests ;)


## License
This project is licensed under the terms of the *GNU General Public License v3.0*. For further information, please look [here](http://choosealicense.com/licenses/gpl-3.0/) or [here<sup>(DE)</sup>](http://www.gnu.org/licenses/gpl-3.0.de.html).
