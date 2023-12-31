<template>
    <div id="scroll-container">
        <div id="page-1" class="page-container">
            <div class="container">
                    <div class="row w-100">
                        <div id="welcome-text" class="col-md-12 col-lg-7">
                            <h1 class="title mt-5" v-motion-slide-visible-top>
                                Welcome to Mokteh Hindun's Homestays
                            </h1>
                            <h3 class="sub-title" v-motion-slide-visible-left>
                                Experience the unparalleled beauty of Terengganu as you immerse yourself in the authentic charm of our Homestay, where every moment becomes a delightful journey into the heart of this enchanting destination. Embrace the rich cultural tapestry, indulge in the vibrant local flavors, and create lasting memories surrounded by the breathtaking landscapes that make your stay a truly unforgettable exploration of Terengganu's allure.
                            </h3>
                        </div>
                        <div id="welcome-pic-list" class="col w-100">
                            <img 
                                v-motion-slide-visible-right
                                id="bridge-pic" 
                                class="welcome-pic" 
                                src="/welcome_pic.jpg" 
                                alt="Jambatan Gantung"
                            />

                            <img 
                                v-motion-pop-visible
                                id="keropok-pic" 
                                class="welcome-pic" 
                                src="/keropok.jpg" 
                                alt="Jambatan Gantung"
                            />
                            
                            <img
                                v-motion-slide-visible-left
                                id="penyu-pic" 
                                class="welcome-pic" 
                                src="/penyu.jpg" 
                                alt="Jambatan Gantung"
                            />
                        </div>
                    </div>
            </div>
        </div>
        <div id="page-2" class="page-container">
            <div class="container">
                    <h1 
                        class="title text-center pt-5" 
                        v-motion-slide-visible-top
                    >
                        What we can offer to you?
                    </h1>
                    <div class="row card-list">
                        <AppBenefits 
                            v-motion-slide-visible-left
                            benefitsTitle="Clean"
                            benefitsText="Indulge in a stay where every corner breathes the freshness of immaculate upkeep."
                            benefitsIconViewBox="0 4 64 64"
                            :benefitsIcon="['M57.08,13.818l-3.687-3.686c-.178-.179-.357-.357-.536-.536a.987.987,0,0,0-1.377,0l-1.715,1.715-4.118,4.118L40.69,20.386l-4.306,4.306c-.477.477-.962.95-1.439,1.428q-.557-.555-1.112-1.112a6.355,6.355,0,0,0-1.167-1.045,2.711,2.711,0,0,0-2.726.019c-.269.156-.531.322-.8.483l-2.558,1.549-.187.114a26.626,26.626,0,0,1-3.8,2.223q-.453.225-.911.436-.233.107-.466.209l-.22.1-.142.06h0c-.719.29-1.439.57-2.175.812-.785.258-1.582.483-2.388.666q-.624.142-1.256.251c-.211.036-.422.068-.633.1l-.157.02c-.129.015-.257.03-.386.043a18.67,18.67,0,0,1-2.953.071c-.267-.016-.533-.037-.8-.066l-.15-.016-.118-.014-.074-.01-.25-.038a15.827,15.827,0,0,1-1.553-.332.889.889,0,0,0-.1-.006A.81.81,0,0,0,7.71,30.6c-.024,0-.046.014-.07.016a.991.991,0,0,0-.192.045,1.092,1.092,0,0,0-.14.046.981.981,0,0,0-.218.141A1.007,1.007,0,0,0,7,30.924a.863.863,0,0,0-.12.167.82.82,0,0,0-.092.188c0,.015-.016.025-.02.04-.007.03,0,.06,0,.09a.73.73,0,0,0-.03.169,25.935,25.935,0,0,0,1.212,6.553c.007.02.01.041.018.06a25.231,25.231,0,0,0,1.872,4.362,24.552,24.552,0,0,0,1.783,2.782c.014.019.032.032.047.05a.925.925,0,0,0,.14.153c.022.019.044.038.067.056a.963.963,0,0,0,.185.117.926.926,0,0,0,.188.064,1.039,1.039,0,0,0,.113.029.922.922,0,0,0,.359-.022,21.633,21.633,0,0,0,2.114-.7c-.042.033-.083.069-.125.1-.02.016-.039.033-.059.048-.231.178-.469.343-.706.511-.12.084-.237.175-.358.257a1,1,0,0,0-.35,1.333.957.957,0,0,0,.282.292,31.892,31.892,0,0,0,7.669,5.928,33.434,33.434,0,0,0,6.926,2.984h0c.708.209,1.421.394,2.141.544a19.854,19.854,0,0,0,5.074.446.984.984,0,0,0,.974-.973,23.366,23.366,0,0,1,1.185-8.7c.384-1.289.832-2.56,1.329-3.81q.151-.38.309-.758c.018-.044.115-.27.011-.027l.081-.189q.09-.211.183-.422.259-.591.535-1.174c.192-.406.387-.812.6-1.208q.633-1.038,1.265-2.075a6.235,6.235,0,0,0,1.274-2.762,3.067,3.067,0,0,0-1.134-2.314l-1.39-1.39L41.576,30.7l4.118-4.118,4.957-4.957,4.307-4.307c.7-.7,1.419-1.374,2.092-2.092l.03-.03A.99.99,0,0,0,57.08,13.818ZM21.886,48.856l0,0C21.833,48.925,21.863,48.886,21.886,48.856Zm15.223-5.75a39.043,39.043,0,0,0-2.425,8.135,23.3,23.3,0,0,0-.363,4.355c-.373,0-.747-.018-1.12-.046-.326-.024-.65-.059-.974-.1l-.145-.019L31.9,55.4c-.218-.034-.436-.072-.653-.112-.572-.107-1.135-.252-1.7-.4a52.709,52.709,0,0,1,1.948-6.466.978.978,0,0,0-.68-1.2,1,1,0,0,0-1.2.68,52.622,52.622,0,0,0-1.938,6.421c-.267-.09-.538-.164-.8-.262-.822-.3-1.37-.531-2.131-.881q-1.08-.5-2.124-1.068c-.209-.114-.408-.245-.615-.363a31.5,31.5,0,0,0,3.215-4.28,27.124,27.124,0,0,0,1.584-2.855,1,1,0,0,0-.349-1.333.982.982,0,0,0-1.332.35,28.954,28.954,0,0,1-2.759,4.578c-.107.146-.215.292-.324.436l-.144.19-.1.121c-.2.261-.414.52-.628.774q-.421.505-.867.989c-.561-.364-1.117-.736-1.655-1.133-.607-.447-1.228-.944-1.88-1.518-.411-.361-.786-.76-1.174-1.146A26.431,26.431,0,0,0,20.55,42.2a1.373,1.373,0,0,0,.184-.3.948.948,0,0,0,.059-.657.908.908,0,0,0-.167-.319.971.971,0,0,0-1.256-.251,24.535,24.535,0,0,1-2.6,1.477q-.612.3-1.237.571l-.167.071-.267.11c-.18.073-.36.145-.541.214-.385.148-.774.293-1.165.426-.176.06-.354.108-.531.163a23.771,23.771,0,0,1-2.63-4.946,24.244,24.244,0,0,0,4.337-.666.974.974,0,0,0-.517-1.878q-1.044.249-2.1.407c-.239.035-.417.057-.756.092q-.393.041-.788.069c-.274.019-.55.034-.825.043a23.394,23.394,0,0,1-.782-4.013,21.109,21.109,0,0,0,9.678-.739,32.725,32.725,0,0,0,7.565-3.39c.245-.148.48-.313.721-.468l3.792,3.792,6.875,6.875,1.092,1.092C38.006,41,37.541,42.048,37.109,43.106Zm3.86-8.206a1.275,1.275,0,0,1,.1.175c0,.015.038.122.047.156,0,0,0,.023.007.042,0,.042,0,.141,0,.156a.268.268,0,0,0,0,.047s-.009,0-.024.061-.012.067-.008.065a.526.526,0,0,0-.034.054c-.022.04-.045.079-.068.118-.172.289-.35.574-.525.86l-.961,1.577-3.475-3.475-6.874-6.875-.7-.7.867-.525,1.24-.751.327-.2.046-.027c.022-.013.116-.057.146-.074.019,0,.251-.051.072-.03.062-.007.122,0,.184-.008l.047,0c.035.01.159.036.192.045l.013,0c.031.016.063.032.093.05s.057.035.085.054c.012.012.038.035.056.054s.033.034.05.051c.126.124.251.25.376.376l1.581,1.58.431.431,3.7,3.7.391.392c.855.855,1.687,1.744,2.571,2.57C40.936,34.864,40.957,34.887,40.969,34.9ZM53.988,15.533,49.87,19.651l-4.957,4.957-4.307,4.307c-.474.474-.965.944-1.443,1.423L36.327,27.5l1.027-1.027,4.117-4.118L46.428,17.4,50.735,13.1c.477-.477.961-.95,1.439-1.428q1.421,1.419,2.84,2.84Z']"
                            benefitsShape="M24.1,-30.4C29.9,-23.9,32.2,-15,32.4,-6.7C32.6,1.5,30.8,9.1,27.6,17.2C24.4,25.3,19.9,33.8,13,36.7C6.2,39.6,-3.1,36.7,-11.3,32.9C-19.4,29.1,-26.5,24.2,-32.2,17.2C-37.9,10.2,-42.2,1,-40.4,-6.7C-38.5,-14.4,-30.5,-20.6,-22.8,-26.7C-15,-32.8,-7.5,-38.8,0.8,-39.8C9.2,-40.8,18.4,-36.9,24.1,-30.4Z"
                            gradientColor1="#D4145A"
                            gradientColor2="#FBB03B"
                        />
                        <AppBenefits 
                            v-motion-pop-visible
                            benefitsTitle="Kampung-vibe"
                            benefitsText="Experience the allure of a traditional village within the heart of Kuala Terengganu."
                            benefitsIconViewBox="-2 -5 40 35"
                            :benefitsIcon="['m20.912 18.228h2.091v2.091h-2.091z', 'm28.14 18.228h2.091v2.091h-2.091z', 'm26.386 10.812v-2.09h-2.898v1.018l1.081 1.073z', 'm33.552 22.112v-4.409h.665l.618-.611-7.322-7.322h-.909v1.269h-2.13l-1.269-1.269h-3.516l-7.314 7.314.618.618h.979v4.409h-1.911c-2.858-2.734-3.618-8.935-3.351-13.548l.047-.094h.023c1.25 0 2.358.606 3.048 1.54l.007.01c.52.703.833 1.588.833 2.545 0 .66-.148 1.285-.414 1.844l.011-.026c.583-.152 1.09-.42 1.518-.78l-.006.005c.898-.786 1.461-1.933 1.461-3.213 0-.955-.314-1.836-.844-2.546l.008.011c-.682-.942-1.777-1.547-3.015-1.547-.386 0-.757.059-1.107.168l.026-.007c.265-.165.57-.311.891-.422l.032-.01c.405-.153.874-.241 1.363-.241 1.083 0 2.064.433 2.781 1.134l-.001-.001c.039-.196.061-.422.061-.653 0-.359-.054-.706-.154-1.032l.007.025c-.521-1.505-1.926-2.566-3.579-2.566-.499 0-.975.097-1.412.273l.025-.009c-.266.093-.489.191-.702.303l.029-.014c-.075-.336-.174-.63-.301-.909l.012.029c-.88-1.973-2.898-2.905-4.511-2.09-.447.231-.815.555-1.09.95l-.006.01c1.189.119 2.199.792 2.779 1.753l.009.016c-.349-.177-.754-.323-1.179-.417l-.034-.006c-2.48-.533-4.84.814-5.263 3.015-.041.206-.064.444-.064.686 0 .392.061.771.173 1.126l-.007-.026c.84-.948 2.06-1.542 3.419-1.542.388 0 .764.048 1.124.14l-.032-.007c.409.086.771.21 1.11.373l-.029-.013c-.163-.023-.351-.036-.542-.036-1.531 0-2.866.836-3.575 2.076l-.011.02c-.404.674-.643 1.488-.643 2.357 0 1.568.777 2.954 1.968 3.794l.015.01c.491.332 1.077.562 1.709.648l.021.002c-.421-.692-.671-1.528-.671-2.423 0-.873.237-1.691.651-2.392l-.012.022c.623-1.073 1.682-1.836 2.927-2.048l.025-.004c-1.417 6.453-1.809 10.949-.64 13.736h-3.406v1.88h32.148v-1.88h-2.169zm-7.95-4.307h7.166v4.307h-7.166zm-10.861-.854 4.95-4.95 4.95 4.95v5.161h-5.435v-3.884h-2.749v3.884h-1.722v-5.161z']"
                            benefitsShape="M24.9,-33.3C31.6,-29.5,35.8,-21.2,36.2,-13.4C36.5,-5.5,33,2.1,30.9,10.5C28.8,18.9,28,28.3,23.1,33.2C18.2,38.1,9.1,38.6,1.2,37C-6.7,35.3,-13.4,31.5,-16.1,25.8C-18.9,20.2,-17.7,12.8,-21.4,5.9C-25,-0.9,-33.4,-7.3,-34.5,-13.5C-35.6,-19.7,-29.5,-25.9,-22.5,-29.7C-15.5,-33.4,-7.8,-34.8,0.7,-35.7C9.1,-36.6,18.3,-37.2,24.9,-33.3Z"
                            gradientColor1="#2E3192"
                            gradientColor2="#1BFFFF"
                        />
                        <AppBenefits 
                            v-motion-slide-visible-right
                            benefitsTitle="Near with city"
                            benefitsText="Enjoy a tranquil retreat just moments away from the vibrant pulse of the city."
                            benefitsIconViewBox="-5 0 64 55"
                            :benefitsIcon="['M10 4L10 20L2.9941406 20L3.1464844 46L17.046875 46L19.046875 46L33 46L47 46L47 8L31 8L31 9L31 28L25.996094 28L25.996094 4.0078125L10 4 z M 12 6L23.996094 6.0078125L23.996094 28L19.013672 28L18.998047 20L18 20L12 20L12 6 z M 15 8L15 10L17 10L17 8L15 8 z M 19.039062 8L19.039062 10L21 10L21 8L19.039062 8 z M 33 10L45 10L45 44L39.960938 44L39.960938 40L38 40L38 44L33 44L33 28L33 10 z M 15 12L15 14L17 14L17 12L15 12 z M 19 12L19 14L21 14L21 12L19 12 z M 36 12.003906L36 14L38 14L38 12.003906L36 12.003906 z M 40.019531 12.007812L40.019531 14.021484L41.980469 14.021484L41.980469 12.007812L40.019531 12.007812 z M 36 16.015625L36 18L38 18L38 16.015625L36 16.015625 z M 40.019531 16.015625L40.019531 18L41.980469 18L41.980469 16.015625L40.019531 16.015625 z M 36 20L36 22L38 22L38 20L36 20 z M 40 20L40 22L41.980469 22L41.980469 20L40 20 z M 5.0058594 22L17.001953 22L17.013672 28L16.998047 28L17.041016 44L11.980469 44L11.980469 40L10.019531 40L10.019531 44L5.1347656 44L5.0058594 22 z M 8 24L8 26.015625L10.039062 26.015625L10.039062 24L8 24 z M 12.039062 24L12.039062 26.015625L14 26.015625L14 24L12.039062 24 z M 36 24.007812L36 25.998047L38 25.998047L38 24.007812L36 24.007812 z M 40 24.007812L40 25.998047L41.980469 25.998047L41.980469 24.007812L40 24.007812 z M 8 27.984375L8 30L10.039062 30L10.039062 27.984375L8 27.984375 z M 12.039062 27.984375L12.039062 30L14 30L14 27.984375L12.039062 27.984375 z M 36 27.992188L36 30.007812L38 30.007812L38 27.992188L36 27.992188 z M 40.019531 27.992188L40.019531 30.007812L41.980469 30.007812L41.980469 27.992188L40.019531 27.992188 z M 19.017578 30L31 30L31 44L26 44L26 40L24 40L24 44L19.042969 44L19.017578 30 z M 8 32L8 34.015625L10.039062 34.015625L10.039062 32L8 32 z M 12.039062 32L12.039062 34.015625L14 34.015625L14 32L12.039062 32 z M 22 32L22 34.015625L24 34.015625L24 32L22 32 z M 26 32L26 34.015625L28 34.015625L28 32L26 32 z M 36 32L36 34.015625L38 34.015625L38 32L36 32 z M 40.019531 32L40.019531 34.015625L41.980469 34.015625L41.980469 32L40.019531 32 z M 22 35.984375L22 38L24 38L24 35.984375L22 35.984375 z M 26 35.984375L26 38L28 38L28 35.984375L26 35.984375 z M 36 35.984375L36 38L38 38L38 35.984375L36 35.984375 z M 40.019531 35.984375L40.019531 38L41.980469 38L41.980469 35.984375L40.019531 35.984375 z']"
                            benefitsShape="M21.2,-19.1C27.2,-9.5,31.4,-0.7,29.7,6.8C28,14.2,20.3,20.3,11.1,25.8C1.8,31.3,-9,36.3,-18.6,33.6C-28.1,30.9,-36.4,20.5,-37.9,9.8C-39.4,-0.9,-34.3,-12.1,-26.8,-22.1C-19.4,-32,-9.7,-40.9,-1,-40.1C7.6,-39.2,15.3,-28.8,21.2,-19.1Z"
                            gradientColor1="#A1C4FD"
                            gradientColor2="#C2E9FB"
                        />
                        <AppBenefits 
                            v-motion-slide-visible-left
                            benefitsTitle="Walkable distance to restaurant"
                            benefitsText="Satisfy your cravings with ease – our homestay is a stone's throw away from a variety of dining options."
                            :benefitsIcon="['M22 1.932v11.068h-2v-11c0-.552-.448-1-1-1s-1 .448-1 1v11h-2v-11.036c0-1.287-2-1.243-2-.033v11.069h-2v-10.99c0-1.363-2-1.313-2-.054v14.472c0 2.087 2 3.463 4 3.463v26.109c0 4 6 4 6 0v-26.108c2 0 4-1.662 4-3.227v-14.701c0-1.275-2-1.226-2-.032zm9 3.068v25h2v16c0 4 7 4 7 0v-41c0-5-9-5-9 0z']"
                            benefitsIconViewBox="-5 -5 64 64"
                            benefitsShape="M19.4,-14.4C27.2,-5.6,37.1,2.5,37.7,12.1C38.3,21.7,29.6,32.6,19.1,36.4C8.6,40.3,-3.8,37,-13.5,31.1C-23.1,25.3,-30,16.9,-33.4,6.4C-36.8,-4.1,-36.7,-16.6,-30.5,-25.1C-24.4,-33.5,-12.2,-37.8,-3.2,-35.3C5.8,-32.7,11.5,-23.3,19.4,-14.4Z"
                            gradientColor1="#EE9CA7"
                            gradientColor2="#FFDDE1"
                        />
                        <AppBenefits
                            v-motion-pop-visible
                            benefitsTitle="Flexible Check-in/Check-out"
                            benefitsText="Experience the convenience of flexible check-in and check-out options tailored to suit your travel schedule."
                            benefitsIconViewBox="-120 -90 1300 1300"
                            :benefitsIcon="['M704 192h160v736H160V192h160.064v64H704v-64zM311.616 537.28l-45.312 45.248L447.36 763.52l316.8-316.8-45.312-45.184L447.36 673.024 311.616 537.28zM384 192V96h256v96H384z']"
                            benefitsShape="M25.3,-17C28.7,-8.7,24.6,1.6,19.1,12.5C13.7,23.4,6.8,35,0.2,34.9C-6.5,34.8,-13,23,-20,11.2C-27.1,-0.6,-34.7,-12.5,-31.5,-20.8C-28.2,-29,-14.1,-33.6,-1.6,-32.6C10.9,-31.7,21.9,-25.3,25.3,-17Z"
                            gradientColor1="#BFF098"
                            gradientColor2="#6FD6FF"
                        />
                        <AppBenefits 
                            v-motion-slide-visible-right
                            benefitsTitle="Extended Stay Discounts"
                            benefitsText="Enjoy special discounts for extended stays, making our homestay an ideal choice for longer, more leisurely visits."
                            benefitsIconViewBox="-5 -10 125 125"
                            :benefitsIcon="['M77.628,25.922c0,1.964-1.59,3.551-3.552,3.551s-3.552-1.587-3.552-3.551c0-1.955,1.59-3.551,3.552-3.551  S77.628,23.968,77.628,25.922z M94.596,7.352l-6.583,6.579c0.054,0.216,0.137,0.421,0.137,0.657l0.226,38.503  c0.005,0.734-0.284,1.44-0.809,1.959L48.42,94.194c-0.534,0.533-1.239,0.803-1.942,0.803c-0.701,0-1.406-0.27-1.94-0.803  L5.806,55.472C5.289,54.952,5,54.252,5,53.521c0-0.725,0.289-1.427,0.806-1.945l39.146-39.139c0.517-0.524,1.144-0.838,1.959-0.809  l38.5,0.226c0.23,0,0.443,0.073,0.656,0.132l6.586-6.579c0.534-0.539,1.406-0.539,1.942,0C95.135,5.941,95.135,6.813,94.596,7.352z   M82.866,51.973l-0.2-34.637l-34.633-0.206L11.643,53.521l34.835,34.838L82.866,51.973z M68.054,47.309L31.43,51.037  c-1.376,0.142-2.383,1.371-2.243,2.754c0.134,1.293,1.225,2.259,2.498,2.259c0.083,0,0.167-0.005,0.255-0.016l36.623-3.729  c1.377-0.137,2.384-1.376,2.246-2.753C70.667,48.176,69.488,47.197,68.054,47.309z M58.575,71.234  c-1.767,2.17-4.385,3.409-7.187,3.409c-2.121,0-4.203-0.734-5.851-2.081c-3.963-3.233-4.556-9.087-1.325-13.04  c1.761-2.165,4.387-3.414,7.186-3.414c2.124,0,4.203,0.739,5.852,2.087C61.215,61.423,61.803,67.276,58.575,71.234z M54.075,62.084  c-0.764-0.622-1.689-0.955-2.677-0.955c-1.283,0-2.486,0.573-3.296,1.567c-1.479,1.813-1.205,4.492,0.61,5.977  c1.751,1.421,4.536,1.146,5.974-0.612C56.162,66.248,55.893,63.568,54.075,62.084z M41.418,32.104  c1.771-2.166,4.389-3.41,7.188-3.41c2.131,0,4.205,0.735,5.854,2.082c3.963,3.228,4.563,9.082,1.33,13.04  c-1.771,2.17-4.392,3.41-7.191,3.41c-2.126,0-4.203-0.735-5.852-2.077C38.787,41.916,38.195,36.067,41.418,32.104z M45.919,41.255  c1.761,1.435,4.543,1.141,5.981-0.607c1.475-1.817,1.2-4.497-0.612-5.977c-0.767-0.627-1.695-0.955-2.682-0.955  c-1.279,0-2.486,0.568-3.294,1.563C43.835,37.091,44.109,39.771,45.919,41.255z']"
                            benefitsShape="M21.1,-14.5C26.2,-3.5,28.2,7,24.1,15.5C20.1,24,10.1,30.6,0.4,30.3C-9.3,30.1,-18.6,23.1,-25.1,13.2C-31.6,3.2,-35.3,-9.6,-30.6,-20.4C-26,-31.3,-13,-40,-2.5,-38.6C8.1,-37.1,16.1,-25.6,21.1,-14.5Z"
                            gradientColor1="#02AABD"
                            gradientColor2="#00CDAC"
                        />
                    </div>
            </div>
        </div>
        <div id="page-3" class="page-container">
            <div class="container">
                <h1 
                    class="title text-center pt-5"
                    v-motion-slide-visible-top
                >
                    Here are the list of our homestay
                </h1>
                <div id="housecard-list" class="row w-100 card-list" v-if="houseDetails">
                    <AppHouseCard 
                        v-for="(item, index) in houseDetails"
                        :key="index"
                        :houseName="transformName(item.name)"
                        :houseImage="backendServer + '/media/' + item.name + '/card/card.jpg'"
                        :housePax="item.pax"
                        :housePricing="item.pricing"
                        :houseBedroom="item.specs.room.length"
                        :houseBathroom="item.specs.bathroom"
                        :houseKitchen="item.specs.kitchen"
                        :houseFridge="item.specs.fridge"
                        :houseKettle="item.specs.kettle"
                        :houseIron="item.specs.iron"
                        :houseUrl="item.name"
                        v-motion-pop-visible="index == 1 ? true : false"
                    />
                </div>
                <div id="housecard-list" class="row w-100 card-list" v-else>
                    <div class="col-lg-4 col mb-5">
                        <v-skeleton-loader
                            class="mx-auto border col-lg-4 col"
                            width="300"
                            height="400"
                            type="image, article"
                        />
                    </div>
                    <div class="col-lg-4 col mb-5">
                        <v-skeleton-loader
                            class="mx-auto border col-lg-4 col"
                            width="300"
                            height="400"
                            type="image, article"
                        />
                    </div>
                    <div class="col-lg-4 col mb-5">
                        <v-skeleton-loader
                            class="mx-auto border col-lg-4 col"
                            width="300"
                            height="400"
                            type="image, article"
                        />
                    </div>
                </div>
            </div>
        </div>
    </div>     
</template>

<script setup>
import AppHouseCard from './../components/AppHouseCard.vue';
import AppBenefits from './../components/AppCard.vue';
import { useHouseStore,  useServerStore } from '@/store/houseStore';
import { ref, onMounted } from 'vue';

const houseStore = useHouseStore();
const houseDetails = ref(null);

const transformName = (name) => {
  return name.replace(/_/g, ' ').replace(/\b\w/g, (match) => match.toUpperCase());
};

onMounted(async () => {
    await houseStore.fetchHouseDetails(useServerStore().backEndServer);
    houseDetails.value = houseStore.houseDetails;
});

const backendServer = useServerStore().backEndServer

</script>


<style scoped>
    #page-1 {
        background: linear-gradient(45deg, #A1C4FD, #C2E9FB);
        scroll-snap-align: start;
    }

    #page-2 {    
        background: linear-gradient(45deg, #FFBBBB, #FDFCFB);
    }

    #page-3 {
        background: linear-gradient(45deg, #93A5CF, #E4EfE9);
    }
    
    #page-1, #page-2, #page-3, #page-4 {
        min-height: calc(100vh);
    }

    #welcome-pic-list {
        margin-top: 14%;
    }

    .welcome-pic {
        height: 400px;
        width: 300px;
        border-radius: 50px;
    }

    .welcome-pic:not(:first-child) {
        margin: -60px 0px;
    }

    .welcome-pic:nth-child(odd) {
        float: right;
    }

    #bridge-pic {    
        rotate: 14deg;
        margin-bottom: -60px;
    }

    #keropok-pic {
        rotate: -14deg;
        margin-left: 30px
    }

    #penyu-pic {    
        rotate: 14deg;
    }

    .card-list {
        margin-top: 100px;
    }

    .v-skeleton-loader__image {
        min-height: 1350px;
    }
    @media (min-width: 992px) {
        html, body {
        height: 100vh !important;
        overflow: hidden !important;
        margin: 0 !important;
        }

        #scroll-container {
        overflow: auto;
        height: calc(100vh);
        scroll-snap-points-y: repeat(100vh);
        scroll-snap-type: y mandatory;
        }

        #page-1, #page-2, #page-3, #page-4 {
        scroll-snap-align: start;
        position: relative;
        will-change: transform;
        }

        #welcome-text {
            margin-top: 30%;
        }
    }

    @media (max-width: 991px) {        
        #welcome-text {
        margin-top: 20px;
        min-height: 0px;
        }

        .title {
            font-size: 75px !important;
        }

        .sub-title {
            font-size: calc(75 / 1.618 * 0.5px)
        }

        #welcome-pic-list {
            margin-top: 90px;
        }

        .welcome-pic {
            position: absolute;
            height: 350px;
            width: 263px;
            border-radius: 20px;
        }

        .welcome-pic:not(:first-child) {
            margin: 0px;
        }

        .welcome-pic:nth-child(odd) {
            float: none;
        }

        #bridge-pic {    
            rotate: -10deg;
            margin: 0px;
            left: 13%
        }

        #keropok-pic {
            rotate: 0deg;
            margin: 0px;
            right: 30%;
        }

        #penyu-pic {    
            rotate: 10deg;
            right: 16%;
        }
    }

    @media (max-width: 768px) {
        #welcome-text {
        margin-top: 10px;
        min-height: 0px;
        }

        .title {
            font-size: 65px !important;
        }

        .sub-title {
            font-size: calc(65 / 1.618 * 0.45px)
        }

        #welcome-pic-list {
            margin-top: 80px;
        }

        .welcome-pic {
            height: 300px;
            width: 226px;
            border-radius: 20px;
        }

        #bridge-pic {    
            rotate: -10deg;
            left: 20%;
        }

        #keropok-pic {
            rotate: deg;
            right: 40%;
        }

        #penyu-pic {    
            rotate: 10deg;
            right: 22%;
        }
    }

    @media (max-width: 576px) {
        #page-1, #page-2, #page-3, #page-4 {
            min-height: max(100vh, 900px);
        }

        #welcome-text {
            margin-top: 10px;
            min-height: 0px;
        }

        .title {
            font-size: 45px !important;
        }

        .sub-title {
            font-size: calc(45 / 1.618 * 0.6px)
        }

        #welcome-pic-list {
            margin-top: 35px;
            margin-bottom: 25px;
        }

        .welcome-pic {
            position: absolute;
            height: 250px;
            width: 192px;
            border-radius: 20px;
        }

        #bridge-pic {    
            rotate: -10deg;
            left: 10%;
        }

        #keropok-pic {
            rotate: deg;
            right: 30%;
        }

        #penyu-pic {    
            rotate: 10deg;
            right: 10%;
        }
    }
</style>