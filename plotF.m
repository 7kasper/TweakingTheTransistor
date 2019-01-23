# ======= Tweaking The Transistor ======= #
#      Script to plot Fmax relations      #
#  By: Arnaud Saint-Genez & Kasper Müller #
# ======= Tweaking The Transistor ======= #

clear;
pkg load io;
fig = figure('name', 'Fmax');

# General Script Options
set(0, "defaultaxesfontname", "Georgia") 
set(0, "defaultaxesfontsize", 12) 
set(0, "defaulttextfontname", "Georgia") 
set(0, "defaulttextfontsize", 12) 

# Read data from sheet
[data] = xlsread('Fdata.xlsx');
Vgs = data(:,1);
Vds = data(:,2);
Ids = data(:,3);
Ta = data(:,4);
Tc = data(:,5);
Trise = data(:,6);
Tfall = data(:,7);
Fmax = data(:,8);

# Read regression constants from sheet
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

# Read Tj formula from other sheet
[Tdata] = xlsread('Tdata.xlsx');
tcA = Tdata(1,5);
# Tj formula
fTj = @(Ta, Tc) ((Tc .- Ta) .* tcA) + Ta;
# Calculate Tj for each point.
Tj = fTj(Ta, Tc);

# Read regression graph options from sheet
precision = data(10, 10);
tjOverflow = data(11, 10);
VdsMin = data(12, 10);
VdsMax = data(13, 10);

# Read style options from sheet
markersize = data(15, 10);

# Read image options from sheet
image = data(17,10);
imageAzimuth = data(18, 10);
imageElevation = data(19, 10);

# Read & define chart bounds
plotVgs = data(:,12);
plotVgs = plotVgs(~isnan(plotVgs));
defT = linspace(min(Tj)-tjOverflow, max(Tj)+tjOverflow, precision);
defVds = linspace(VdsMin, VdsMax, precision);
[RegTj, RegVds] = meshgrid(defT, defVds);
# Color
caxis([min(Vgs), max(Vgs)]);

# Plot raw data
scatter3(Tj, Vds, Fmax, markersize, Vgs, 'filled', 'MarkerEdgeColor', [0,0,0]);
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
  PlotColor = regVgs .+ RegFmax .- RegFmax;
  # Draw
  m = mesh(RegTj, RegVds, RegFmax, PlotColor, 'facealpha', 0.1, 'facecolor', 'none');
  #Fake draw for legend stuff.
  p = scatter(max(Tj), 0, markersize, regVgs, 'filled', 'MarkerEdgeColor', [0,0,0]);
  hh = [hh, p];
  hidden on;
endfor

# Hide fake draw with white scatter plot. Why not?
scatter(max(Tj), 0, markersize, [1,1,1], 'filled', 'MarkerEdgeColor', [1,1,1]);

# Set further chart options
legend(hh, legends);
title('Relations to Fmax');
xlabel('Tj (K)');
ylabel('Vds (V)');
zlabel('Fmax (MHz)');

view([imageAzimuth, imageElevation]);

# Finish to save.
hold off;

# Save graph image if specified
if (image > 0)
  saveas(fig, ['snapshot-' num2str(image)], 'png')
  #print(['snapshot-' num2str(image)], '-dsvg');
endif
