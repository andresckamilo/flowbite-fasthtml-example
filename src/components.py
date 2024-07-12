from fasthtml.common import *

def hero_section():
    return Title("Fast HMTL"), Body(
  Nav(
    Div(
      A(
        Img(src='https://flowbite.com/docs/images/logo.svg', cls='h-6 mr-3 sm:h-9', alt='Flowbite Logo'),
        Span('Flowbite', cls='self-center text-xl font-semibold whitespace-nowrap dark:text-white'),
        href='https://flowbite.com/',
        cls='flex items-center'
      ),
      Div(
        Button('Get\n                    started', type='button', cls='text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center mr-3 md:mr-0 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800'),
        Button(
          Span('Open main menu', cls='sr-only'),
          Svg(
            Path(fill_rule='evenodd', d='M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 15a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z', clip_rule='evenodd'),
            cls='w-6 h-6',
            aria_hidden='true',
            fill='currentColor',
            viewbox='0 0 20 20',
            xmlns='http://www.w3.org/2000/svg'
          ),
          data_collapse_toggle='navbar-cta',
          type='button',
          cls='inline-flex items-center p-2 text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600',
          aria_controls='navbar-cta',
          aria_expanded='false'
        ),
        cls='flex md:order-2'
      ),
      Div(
        Ul(
          Li(
            A('Home', href='#', cls='block py-2 pl-3 pr-4 text-white bg-blue-700 rounded md:bg-transparent md:text-blue-700 md:p-0 dark:text-white', aria_current='page')
          ),
          Li(
            A('About', href='#', cls='block py-2 pl-3 pr-4 text-gray-700 rounded hover:bg-gray-100 md:hover:bg-transparent md:hover:text-blue-700 md:p-0 md:dark:hover:text-white dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700')
          ),
          Li(
            A('Services', href='#', cls='block py-2 pl-3 pr-4 text-gray-700 rounded hover:bg-gray-100 md:hover:bg-transparent md:hover:text-blue-700 md:p-0 md:dark:hover:text-white dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700')
          ),
          Li(
            A('Contact', href='#', cls='block py-2 pl-3 pr-4 text-gray-700 rounded hover:bg-gray-100 md:hover:bg-transparent md:hover:text-blue-700 md:p-0 md:dark:hover:text-white dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700')
          ),
          cls='flex flex-col p-4 mt-4 border border-gray-100 rounded-lg bg-gray-50 md:flex-row md:space-x-8 md:mt-0 md:text-sm md:font-medium md:border-0 md:bg-white dark:bg-gray-800 md:dark:bg-gray-900 dark:border-gray-700'
        ),
        cls='items-center justify-between hidden w-full md:flex md:w-auto md:order-1',
        id='navbar-cta'
      ),
      cls='container flex flex-wrap items-center justify-between mx-auto'
    ),
    cls='bg-white border-gray-200 px-2 sm:px-4 py-2.5 rounded dark:bg-gray-900'
  ),
  Section(
    Div(
      Div(
        H1('Payments tool for software companies', cls='max-w-2xl mb-4 text-4xl font-extrabold leading-none tracking-tight md:text-5xl xl:text-6xl dark:text-white'),
        P('From checkout to global sales tax compliance, companies around the world use Flowbite to simplify their payment stack.', cls='max-w-2xl mb-6 text-gray-500 lg:mb-8 md:text-lg lg:text-xl dark:text-gray-400'),
        A(
          'Get started',
          Svg(
            Path(fill_rule='evenodd', d='M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z', clip_rule='evenodd'),
            cls='w-5 h-5 ml-2 -mr-1',
            fill='currentColor',
            viewbox='0 0 20 20',
            xmlns='http://www.w3.org/2000/svg'
          ),
          href='#',
          cls='inline-flex items-center justify-center px-5 py-3 mr-3 text-base font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 dark:focus:ring-blue-900'
        ),
        A('Speak to Sales', href='#', cls='inline-flex items-center justify-center px-5 py-3 text-base font-medium text-center text-gray-900 border border-gray-300 rounded-lg hover:bg-gray-100 focus:ring-4 focus:ring-gray-100 dark:text-white dark:border-gray-700 dark:hover:bg-gray-700 dark:focus:ring-gray-800'),
        cls='mr-auto place-self-center lg:col-span-7'
      ),
      Div(
        Img(src='https://flowbite.s3.amazonaws.com/blocks/marketing-ui/hero/phone-mockup.png', alt='mockup'),
        cls='hidden lg:mt-0 lg:col-span-5 lg:flex'
      ),
      cls='grid max-w-screen-xl px-4 py-8 mx-auto lg:gap-8 xl:gap-0 lg:py-16 lg:grid-cols-12'
    ),
    cls='bg-white dark:bg-gray-900'
  ),
  Script(src='https://cdn.jsdelivr.net/npm/flowbite@2.4.1/dist/flowbite.min.js')
)