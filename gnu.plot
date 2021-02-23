set title system("cd ../; printf '%s\n' ${PWD##*/}") font ",20"
set xlabel "Time"
set ylabel "FPS"
set datafile separator ','
set key left box
set terminal pngcairo size 800,600 enhanced color font 'Segoe UI,10'
set colorsequence classic
set output 'plot.png'
plot for [col=1:*] 'frames/graph_me.csv' using col with lines title col