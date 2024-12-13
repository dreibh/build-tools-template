PORTNAME=	td-build-tools-template
DISTVERSION=	0.0.0
CATEGORIES=	devel
MASTER_SITES=	https://www.nntb.no/~dreibh/build-tools/download/

MAINTAINER=	thomas.dreibholz@gmail.com
COMMENT=	A a simple example program to be build and packaged by Build Tool
WWW=		https://www.nntb.no/~dreibh/build-tools/

LICENSE=	GPLv3+
LICENSE_FILE=	${WRKSRC}/COPYING

RUN_DEPENDS=

USES=		cmake gettext tar:xz
CMAKE_ARGS=	-DCMAKE_INSTALL_MANDIR=${PREFIX}/share/man

.include <bsd.port.mk>
