/* filename: pi.h - DLL version */
#ifndef PI_H
#define PI_H

#ifdef _WIN32
    #ifdef BUILDING_PI_DLL
        #define PI_API __declspec(dllexport)
    #else
        #define PI_API __declspec(dllimport)
    #endif
#else
    #define PI_API
#endif

PI_API float pi_approx(int n);

#endif /* PI_H */
