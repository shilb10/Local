% mphandout.cls: A class for CS MP handouts.
% Copyright (C) 2002 Ava Jarvis <ajar@katanalynx.dyndns.org>
% 
% This program is free software; you can redistribute it and/or
% modify it under the terms of the GNU General Public License
% as published by the Free Software Foundation; either version 2
% of the License, or (at your option) any later version.
% 
% This program is distributed in the hope that it will be useful,
% but WITHOUT ANY WARRANTY; without even the implied warranty of
% MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
% GNU General Public License for more details.
% 
% You should have received a copy of the GNU General Public License
% along with this program; if not, write to the Free Software
% Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
%
\NeedsTeXFormat{LaTeX2e}[1995/12/01]
\ProvidesClass{mphandout}[2002/07/01 v1.0 Class for CS MP handouts]
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
\ProcessOptions\relax
\LoadClass{article}

\RequirePackage{fullpage}
\RequirePackage{fancyvrb}
\RequirePackage{times}

\DefineVerbatimEnvironment%
{LitVerbatim}{Verbatim}
{frame=leftline, numbers=none, firstnumber=last, numbersep=3pt, 
 gobble=0, commandchars=\\\{\}}

\DefineVerbatimEnvironment%
{CodeVerbatim}{Verbatim}
{numbers=none, firstnumber=last, gobble=0,commandchars=\\\{\}}

\newcounter{problem}
\newenvironment{problem}%
  {\stepcounter{problem}
   \begin{list}{}
   {\settowidth{\labelwidth}{00}
    \setlength{\leftmargin}{\labelwidth}
    \addtolength{\leftmargin}{\labelsep}
    \renewcommand{\makelabel}{\theproblem.}}
    \item}
  {\end{list}\vspace{1em}}

\newcommand{\cproblem}[1]%
  {\begin{problem}#1\end{problem}}

\def\given#1{\gdef\@given{#1}}
\def\due#1{\gdef\@due{#1}}
\def\extend#1{\gdef\@extend{#1}}
\def\revision#1{\gdef\@revision{#1}}
\def\class#1{\gdef\@class{#1}}

\renewcommand{\maketitle}{%
\hrule
\vskip 1em

\begin{center}
\Huge \@title \\
\Large \@class \\
\large Revision \@revision \\ [1em]

\begin{tabular}{l}
\textbf{Assigned} \@given \\
\textbf{Due} \@due \\
\textbf{Extension} \@extend
\end{tabular}

\end{center}

\hrule
}


%% End of file `mphandout.cls'.
