// qx11embed_x11.sip generated by MetaSIP
//
// This file is part of the QtGui Python extension module.
//
// Copyright (c) 2016 Riverbank Computing Limited <info@riverbankcomputing.com>
// 
// This file is part of PyQt4.
// 
// This file may be used under the terms of the GNU General Public License
// version 3.0 as published by the Free Software Foundation and appearing in
// the file LICENSE included in the packaging of this file.  Please review the
// following information to ensure the GNU General Public License version 3.0
// requirements will be met: http://www.gnu.org/copyleft/gpl.html.
// 
// If you do not wish to use this file under the terms of the GPL version 3.0
// then you may purchase a commercial license.  For more information contact
// info@riverbankcomputing.com.
// 
// This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
// WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.


%If (- Qt_5_0_0)
%If (WS_X11)

class QX11EmbedWidget : QWidget
{
%TypeHeaderCode
#include <qx11embed_x11.h>
%End

public:
    enum Error
    {
        Unknown,
        Internal,
        InvalidWindowID,
    };

    QX11EmbedWidget(QWidget *parent /TransferThis/ = 0);
    virtual ~QX11EmbedWidget();
    void embedInto(WId id);
    WId containerWinId() const;
%If (Qt_4_2_0 -)
    QX11EmbedWidget::Error error() const;
%End

signals:
    void containerClosed();
    void embedded();
    void error(QX11EmbedWidget::Error error);

protected:
    virtual bool eventFilter(QObject *, QEvent *);
    virtual bool event(QEvent *);
    virtual void resizeEvent(QResizeEvent *);

private:
    QX11EmbedWidget(const QX11EmbedWidget &);
};

%End
%End
%If (- Qt_5_0_0)
%If (WS_X11)

class QX11EmbedContainer : QWidget
{
%TypeHeaderCode
#include <qx11embed_x11.h>
%End

public:
    enum Error
    {
        Unknown,
        Internal,
        InvalidWindowID,
    };

    QX11EmbedContainer(QWidget *parent /TransferThis/ = 0);
    virtual ~QX11EmbedContainer();
    WId clientWinId() const;
    void discardClient();
    void embedClient(WId id);
%If (Qt_4_2_0 -)
    QX11EmbedContainer::Error error() const;
%End
    virtual QSize minimumSizeHint() const;

signals:
    void clientClosed();
    void clientIsEmbedded();
    void error(QX11EmbedContainer::Error);

protected:
    virtual bool eventFilter(QObject *, QEvent *);
    virtual void paintEvent(QPaintEvent *e);
    virtual void resizeEvent(QResizeEvent *);
    virtual void showEvent(QShowEvent *);
    virtual void hideEvent(QHideEvent *);
    virtual bool event(QEvent *);

private:
    QX11EmbedContainer(const QX11EmbedContainer &);
};

%End
%End
