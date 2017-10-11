" If no screen, use color term
if ($TERM == "vt100")
	" xterm-color / screen
	set t_Co=8
	set t_AF=[1;3%p1%dm
	t t_AB=[4%p1%dm
endif

if filereadable($VIMRUNTIME . "/vimrc_example.vim")
	so $VIMRUNTIME/vimrc_example.vim
endif

if filereadable($VIMRUNTIME . "/macros/matchit.vim")
	so $VIMRUNTIME/macros/matchit.vim
endif

syntax on

set nocompatible
set wildmenu
set backupdir=~/tmp,.,/var/tmp/vi.recover,/tmp
set directory=~/tmp,/var/tmp/vi.recover,/tmp,.
set backup		" keep a backup file
" set textwidth=78
" set shiftwidth=4
"set bs2		" allow backspacing over everything in insert mode
set autoindent			" always set autoindenting on
set nu
set ts=4
set expandtab
set viminfo='20,\"50	" read/write a .viminfo file, don't store more
set showmatch

"set background=dark	" another is 'light'

" VIM 6.0,
if version >= 600
	set nohlsearch
	" set foldcolumn=2
	" set foldmethod=syntax
	set foldmethod=marker
	set foldlevel=1
	"    set foldtext=/^/=>
	set encoding=utf-8
	set fileencoding=utf-8
	" set termencoding=big5
	" set encoding=big5
	" set fileencodings=latin,big5,ucs-bom,utf-8,sjis,big5
	set fileencodings=ucs-bom,utf-8,sjis,big5,latin1
else
	set fileencoding=utf-8
endif

" Tab key binding
if version >= 700
	map  <C-c> :tabnew<CR>
	imap <C-c> <ESC>:tabnew<CR>
	map  <C-k> :tabclose<CR>
	map  <C-p> :tabprev<CR>
	imap <C-p> <ESC>:tabprev<CR>
	map  <C-n> :tabnext<CR>
	"imap <C-n> <ESC>:tabnext<CR>
	map <F4> :set invcursorline<CR>

	map g1 :tabn 1<CR>
	map g2 :tabn 2<CR>
	map g3 :tabn 3<CR>
	map g4 :tabn 4<CR>
	map g5 :tabn 5<CR>
	map g6 :tabn 6<CR>
	map g7 :tabn 7<CR>
	map g8 :tabn 8<CR>
	map g9 :tabn 9<CR>
	map g0 :tabn 10<CR>
	map gc :tabnew<CR>
	map gn :tabn<CR>
	map gp :tabp<CR>

	highlight TabLineSel term=bold,underline cterm=bold,underline ctermfg=7 ctermbg=0
	highlight TabLine    term=bold cterm=bold
	highlight clear TabLineFill


end

" Crontabs must be edited in place
au BufRead /tmp/crontab* :set backupcopy=yes
set sw=4 ts=4 sts=4


set smartindent
inoremap ( ()<LEFT>
inoremap { {}<LEFT>
inoremap " ""<LEFT>
inoremap [ []<LEFT>
set tabstop=4
set softtabstop=4
set shiftwidth=4
set smarttab
set cindent

highlight ExtraWhitespace ctermbg=lightgray ctermfg=black guibg=lightgray
match Todo /\s\+$/

set nobackup
set nowritebackup
set noswapfile

filetype plugin indent on
" show existing tab with 4 spaces width
set tabstop=4
" when indenting with '>', use 4 spaces width
set shiftwidth=4
" On pressing tab, insert 4 spaces
set expandtab"""

colorscheme default

"highlight long lines
let &colorcolumn=join(range(81,999),",")
highlight ColorColumn ctermbg=237 guibg=#2c2d27

map <S-j> <C-W>j<C-W>
map <S-h> <C-W>h<C-W>
map <S-k> <C-W>k<C-W>
map <S-l> <C-W>l<C-W>
