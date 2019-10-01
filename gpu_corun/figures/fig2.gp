set terminal png size 800,500 enhanced font "Helvetica,16"
set output 'fig2.png'

set style data histogram 
set xtics rotate out
set style fill solid border -1
set boxwidth 2 absolute 
#set xtic format ""
set title "LC Degradation without Preemption"
unset key
set xtics nomirror
#set ytics ["0", "5X", "10X", "15X", "20X", "25X", "30X"] 
set bars front
set yrange [0:30]
set ytics ("0" 0, "10X" 10,  "20X" 20, "30X" 30)
set xrange [-1:35.5]
plot "fig2.txt" using 2:xticlabels(1) lc "blue", "fig21.txt" using 1:2 with line linetype 3 lw 3 dashtype '..-' lc "red"
