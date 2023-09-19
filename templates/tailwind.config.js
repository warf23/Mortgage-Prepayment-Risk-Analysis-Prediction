/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js}"],
  extend: {
    fontFamily: {
      'roboto-slab': ['Roboto Slab', 'serif'],
    },
    height: { //
      '133': '133px',
      '44': '44px' , 
      'landing-hight': '40rem' ,

    },
    width: { 
      '133': '133px',

    },
   
    
    colors: {
      primary: '#2563EB', // Add your new primary color here
      white: '#FFFFFF',
    },
  },
  plugins: [
    // ...
    require('@tailwindcss/forms'),
  ],
}