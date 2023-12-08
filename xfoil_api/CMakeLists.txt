cmake_minimum_required(VERSION 3.10)
project(xfoil Fortran)

enable_language(Fortran)
if (${CMAKE_Fortran_COMPILER_ID} MATCHES "GNU")
	set(CMAKE_Fortran_FLAGS "${CMAKE_Fortran_FLAGS} \
		-O3 \
		-fbounds-check \
		-finit-real=inf \
		-ffpe-trap=invalid,zero \
		-fdefault-real-8 \
		-static \
		-static-libgfortran -static-libgcc "
	)
else()
   set (CMAKE_Fortran_FLAGS "${CMAKE_Fortran_FLAGS} \
		-Ofast \
		-check bounds \
                -fpe0 \
                -fpp \
                -r8 \
		-static \
		-static-intel "
	)
endif()

add_library(xfoil SHARED
        # Include modules
        src/i_pindex.f90
        src/i_xfoil.f90
        src/i_blpar.f90
        src/i_circle.f90
        src/i_xbl.f90
        # Shared modules to avoid circular dependencies
        src/s_xbl.f90
        src/s_xoper.f90
        src/s_xfoil.f90
        # Main modules
        src/m_aread.f90
        src/m_iopol.f90
        src/m_naca.f90
        src/m_sort.f90
        src/m_spline.f90
        src/m_userio.f90
        src/m_xbl.f90
        src/m_xblsys.f90
        src/m_xfoil.f90
        src/m_xgdes.f90
        src/m_xgeom.f90
        src/m_xmdes.f90
        src/m_xoper.f90
        src/m_xpanel.f90
        src/m_xpol.f90
        src/m_xqdes.f90
        src/m_xsolve.f90
        src/m_xutils.f90
        # API
        src/api.f90)

# Add cpack

#include(CPack)
#set(CPACK_PACKAGE_NAME "xfoil")
#set(CPACK_PACKAGE_VERSION "1.0.0")
#set(CPACK_GENERATOR "NSIS")  # You can change this to other generators like DEB, RPM, etc.
#
## Add any other CPack configurations as needed
## For example, setting the package description, author, etc.
#set(CPACK_PACKAGE_DESCRIPTION_SUMMARY "Your package description summary")
#set(CPACK_PACKAGE_VENDOR "Your vendor name")
#set(CPACK_PACKAGE_DESCRIPTION_FILE "${CMAKE_CURRENT_SOURCE_DIR}/README.md")
#set(CPACK_RESOURCE_FILE_LICENSE "${CMAKE_CURRENT_SOURCE_DIR}/LICENSE")
#
#
#add_custom_target(build_and_package
#    COMMAND ${CMAKE_COMMAND} --build ${CMAKE_BINARY_DIR} --target all
#    COMMAND ${CMAKE_COMMAND} --build ${CMAKE_BINARY_DIR} --target package
#    COMMENT "Building and packaging xfoil")
#
