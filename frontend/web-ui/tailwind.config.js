export default {
  content: ['./index.html', './src/**/*.{ts,tsx}'],
  theme: {
    extend: {
      boxShadow: {
        glow: '0 30px 80px rgba(139,92,246,0.24)',
      },
      backgroundImage: {
        radialGlow: 'radial-gradient(circle at top left, rgba(139,92,246,0.22), transparent 32%), radial-gradient(circle at bottom right, rgba(34,197,94,0.16), transparent 28%)',
      },
      animation: {
        float: 'float 8s ease-in-out infinite',
      },
      keyframes: {
        float: {
          '0%, 100%': { transform: 'translateY(0px)' },
          '50%': { transform: 'translateY(-10px)' },
        },
      },
    },
  },
  plugins: [],
}
