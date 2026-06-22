import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

# Initialize canvas with a 16:9 aspect ratio and pure black background
fig, ax = plt.subplots(figsize=(16, 9), facecolor='#000000')
ax.set_facecolor('#000000')

# Set structural limits
ax.set_xlim(-10, 10)
ax.set_ylim(-5.625, 5.625)
ax.axis('off')

# 1. Generate Isometric Background Grid (Fine White Lines)
grid_color = '#111111'
line_weight = 0.5

# Isometric angles (30 and 150 degrees)
theta1 = np.radians(30)
theta2 = np.radians(150)

for clip in np.linspace(-20, 20, 60):
    # Forward isometric lines
    ax.plot([-20, 20], [-20 * np.tan(theta1) + clip, 20 * np.tan(theta1) + clip], color=grid_color, lw=line_weight, zorder=1)
    # Backward isometric lines
    ax.plot([-20, 20], [-20 * np.tan(theta2) + clip, 20 * np.tan(theta2) + clip], color=grid_color, lw=line_weight, zorder=1)

# 2. Plot Unfolding Intertwined Heptagons (7-Sided Polygons)
def get_heptagon_vertices(cx, cy, r, rotation_deg):
    angles = np.linspace(0, 2 * np.pi, 8) + np.radians(rotation_deg)
    x = cx + r * np.cos(angles)
    y = cy + r * np.sin(angles)
    return x, y

center_x, center_y = 0, 0
num_heptagons = 6
base_radius = 1.2
neon_cyan = '#00E5FF'
pure_white = '#FFFFFF'

for i in range(1, num_heptagons + 1):
    r = base_radius * (i ** 1.3)
    # Subtle rotation per layer creates the "unfolding/intertwined" torsional effect
    rot = i * 7.5  
    x, y = get_heptagon_vertices(center_x, center_y, r, rot)
    
    # Draw primary structural frame
    ax.plot(x, y, color=pure_white, lw=1.2, alpha=0.85 - (i * 0.08), zorder=3)
    
    # Highlight vertex interconnections with neon cyan nodes
    ax.scatter(x[:-1], y[:-1], color=neon_cyan, s=15 + (i * 5), alpha=0.9, zorder=4, edgecolors='none')

# 3. Add Precise Technical Annotations & Equations (Register 1 & 2 Verification)
text_params = {'color': pure_white, 'fontsize': 13, 'usetex': False, 'fontfamily': 'monospace'}

# Annotation 1: Fine Structure Constant Derivation
ax.annotate(r'$\alpha^{-1} \approx 137.0354$', xy=(0, 1.2), xytext=(-6, 3.5),
            arrowprops=dict(arrowstyle="->", color=neon_cyan, lw=0.8, connectionstyle="arc3,rad=-0.1"),
            **text_params)

# Annotation 2: Metric Determinant Invariance Constraint
ax.annotate(r'$\det(g_{\mu\nu}) \neq 0 \quad [4.5 : 1.5]$', xy=(2.2, -1.1), xytext=(4, -3),
            arrowprops=dict(arrowstyle="->", color=neon_cyan, lw=0.8, connectionstyle="arc3,rad=0.1"),
            **text_params)

# Annotation 3: Predictive Empathy Tensor Invariant
ax.annotate(r'$E_{AB} = \nabla_A A_B^{(H)} - \nabla_B A_A^{(H)}$', xy=(-1.5, -2.1), xytext=(-8, -2.5),
            arrowprops=dict(arrowstyle="->", color=neon_cyan, lw=0.8, connectionstyle="arc3,rad=-0.05"),
            **text_params)

# Annotation 4: Torsional Shear Deficit
ax.annotate(r'$\delta_{\mathrm{shear}} = 1 - \frac{1}{\pi} \approx 0.681690$', xy=(3.8, 1.8), xytext=(4.5, 2.5),
            arrowprops=dict(arrowstyle="->", color=neon_cyan, lw=0.8, connectionstyle="arc3,rad=0.0"),
            **text_params)

# Annotation 5: Bulk Metric Conformal Factor
ax.text(-8, 4.5, r'$G_{MN}(x,t) = \psi(\Omega_0 t)G_{MN}(x)$', **text_params)
ax.text(3.5, -4.5, r'$\partial^A T^{(\beta)}_{AB} = 0$', **text_params)

# Save image configuration
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
plt.savefig('huft_github_header.png', dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
