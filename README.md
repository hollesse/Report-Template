# DHBW - LaTeX - Template
Please use XeLaTeX or LuaLaTex for building.


## Features
- all formal layout-properties of the document are in accordance to the requirements given by the Technical Faculty of DHBW Mannheim.
- Titlepages for Internship Reports, Study Reports and Bachelor Thesis in accordance to these requirements included

<img alt="various Titlepages" src="http://i.imgur.com/ddOe000.png" width="70%">

- Fully customizable coloring

<img alt="Coloring" src="http://i.imgur.com/TGjZShi.png" width="70%">

- Easy switching between the (default) *english* and *german* version of the document


## How to Setup and Use
1. inside `./setup.tex`:
    - choose the type of your Report
    - choose if you want to write your report in english or german
    - fill out the fields for your informations
    - choose your desired color theme or define your own
2. places the entries for your bibliography into `./resources/references.bib`
3. place the `.tex`-files containing your content into `./content` and define the structure of your content inside `./content/structure.tex`
4. fill your acronyms and custom macros as needed into `./content/acronyms.tex` and `./content/macros.tex`
5. save your image files into `./resources`
    - you can then use them easily by just referencing `\includegraphics{asdf}` if you saved your file at `./resources/asdf.png`


## Included Custom Elements for Ease of Use
#### striped Tables
```Latex
\begin{stripedacenttable}
    {formating}
    {Headings-Content}
    row definitions
\end{stripedacenttable}

\begin{stripedtable}
    {coloring}
    {formating}
    {Headings-Content}
    row definitions
\end{stripedtable}
```

- formating should have the form `x^x^x^...` where `x` specifies the alignment for the column
    + possible aligments: `l`: left-aligned , `c`: centered , `r`: right-aligned

> *Example (with captions):*
> ```Latex
\begin{table}[htbp]
    \begin{stripedacenttable}
        {c^l^l}
        {Quarter & asdf & foobar}
        prev. Year & 42 & 17 \\
        Q1 & -3 & -7 \\
        Q2 & +7 & -1 \\
        Q3 & -4 & +12 \\
        Q4 & +2 & +2 \\
    \end{stripedacenttable}
    \caption{A plain but nice looking table}
    \label{tab:ex1}
\end{table}

> Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Ut purus elit, vestibulum ut, placerat ac, adipiscing vitae, felis.

> \begin{table}[htbp]
    \begin{stripedtable}
        {Green}
        {c^l^l}
        {Quarter & asdf & foobar}
        prev. Year & 42 & 17 \\
        Q1 & -3 & -7 \\
        Q2 & +7 & -1 \\
        Q3 & -4 & +12 \\
        Q4 & +2 & +2 \\
    \end{stripedtable}
    \caption{A colorful, nice looking table}
    \label{tab:ex2}
\end{table}
```

> <img alt="Tables" src="http://i.imgur.com/A1EaX51.png" width="45%">

#### Code Listings
```Latex
\begin{lstlisting}[
    caption={description of your program}
    \label{lst:name},
    captionpos=b,
    language=language-name
]
your code
\end{lstlisting}
```

> *Example:*

> ```Latex
\begin{lstlisting}[
    caption={The Classic, realized in Python}
    \label{lst:python1},
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

#### Citations in the Footnotes
````Latex
\footnotecite{source}
```

#### Prevent Pagebreaks absolutely, definitively
```Latex
\begin{absolutelynopagebreak}
    content
\end{absolutelynopagebreak}
```


---


## Contributing
I'm open for all forks, feedback and Pull Requests ;)
