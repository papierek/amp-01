

Rvol 7 1 1
Rin 1 gnd 20k

R1 2 gnd 20k
C1 1 2 4.7u
R2 2 3 1k
C2 3 gnd 680p

Rout 3 gnd 100000Meg

vin 7 gnd dc 0 ac 1

.ac dec 100 1 100k
.control
run
plot vdb(3) xlog
.endc
.end

