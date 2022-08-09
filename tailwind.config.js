module.exports = {
  content: ["./templates/*{html,js}"],
  theme: {
    extend: {
      colors: {
        primaryColor: '#9381FF',
        secondaryColor: '#F8F7FF',
        backgroundColor: '#8670FF'
      },
    },

    borderWidth: {
      DEFAULT: '0px',
      '0': '0',
      '2': '2px',
      '3': '3px',
      '4': '4px',
      '6': '6px',
      '8': '8px',
    },
      fontFamily: {
        'roboto': ['Roboto', 'sans-serif'],
        'inter': ['Inter', 'sans-serif'],
        'cedarville': ['Cedarville Cursive']
    },
  },
  plugins: [],
}