# ======= Tweaking The Transistor ======= #
#      Script to plot Fmax relations      #
#  By: Arnaud Saint-Genez & Kasper Müller #
# ======= Tweaking The Transistor ======= #

clear;
pkg load io;
figure('name', 'Fmax');

# Read data from sheat
[data] = xlsread('Fdata.xlsx');
Vgs = data(:,1);
Vds = data(:,2);
Ids = data(:,3);
Ta = data(:,4);
Tc = data(:,5);
Trise = data(:,6);
Tfall = data(:,7);
Fmax = data(:,8);

# Read regression constants from sheat
cA = data(1,10);
cB = data(2,10);
cC = data(3,10);
cD = data(4,10);
cE = data(5,10);
pT = data(6,10);
qT = data(7,10);
qV = data(8,10);
# Define fmax formula with constants
f = @(Vgs, Vds, Tj) cA ./ (((((Tj ./ pT) .^ qT) ./ ((Vgs .- cB) .^ qV)) .+ cC) .* log(cD .* Vds .+ cE));

# Read Tj formula from other sheat
[Tdata] = xlsread('Tdata.xlsx');
tcA = Tdata(1,5);
# Tj formula
fTj = @(Ta, Tc) ((Tc .- Ta) .* tcA) + Ta;
# Calculate Tj for each point.
Tj = fTj(Ta, Tc);

# Read graph options from sheat
precision = data(10, 10);
tjOverflow = data(11, 10);
VdsMin = data(12, 10);
VdsMax = data(13, 10);
markersize = data(15, 10);

# Read & define chart bounds
plotVgs = data(:,12);
plotVgs = plotVgs(~isnan(plotVgs));
defT = linspace(min(Tj)-tjOverflow, max(Tj)+tjOverflow, precision);
defVds = linspace(VdsMin, VdsMax, precision);
[RegTj, RegVds] = meshgrid(defT, defVds);
# Color
caxis([0, 1]);
VgsColor = @(Vgs, min, max) (Vgs .- min) .* (1 / (max - min));
FmaxColor = @(Fmax) (Fmax .- min(Fmax)) .* (1 ./ (max(Fmax) - min(Fmax)));

# Plot raw data
scatter3(Tj, Vds, Fmax, markersize, VgsColor(Vgs, min(Vgs), max(Vgs)), 'filled');
hold on;

# Legend reference.
legends = [''];
hh = []; #Legend headers

# Plot regression graphs
for regVgs = plotVgs'
    legends = [legends; ['Vgs: ' num2str(regVgs, 3)] 'V'];
    # Calculate fmax for this Vgs:
    RegFmax = f(regVgs, RegVds, RegTj);
    
    # Color
    PlotColor = VgsColor(regVgs, min(Vgs), max(Vgs)) .+ RegFmax .- RegFmax;
    
    # Draw
    m = mesh(RegTj, RegVds, RegFmax, PlotColor, 'facealpha', 1, 'facecolor', 'none');
    
    #Fake draw for legend stuff.
    p = scatter(max(Tj), max(Vds), markersize, VgsColor(regVgs, min(Vgs), max(Vgs)), 'filled');
    hh = [hh, p];
    
    hidden on;
endfor

# Hide fake draw with white scatter plot. Why not?
scatter(max(Tj), max(Vds), markersize, [1,1,1], 'filled');

leg = legend(hh, legends);
set (leg);

title('Relations to Fmax');
xlabel('Tj (Kelvin)');
ylabel('Vds (Volt)');
zlabel('Fmax (Hz)');
