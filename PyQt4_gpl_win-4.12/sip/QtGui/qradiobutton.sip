// qradiobutton.sip generated by MetaSIP
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


class QRadioButton : QAbstractButton
{
%TypeHeaderCode
#include <qradiobutton.h>
%End

public:
    explicit QRadioButton(QWidget *parent /TransferThis/ = 0);
    QRadioButton(const QString &text, QWidget *parent /TransferThis/ = 0);
%If (Qt_5_0_0 -)
    virtual ~QRadioButton();
%End
    virtual QSize sizeHint() const;
%If (Qt_4_8_0 -)
    virtual QSize minimumSizeHint() const;
%End

protected:
%If (Qt_4_3_0 -)
    void initStyleOption(QStyleOptionButton *button) const;
%End
    virtual bool hitButton(const QPoint &) const;
    virtual bool event(QEvent *e);
    virtual void paintEvent(QPaintEvent *);
    virtual void mouseMoveEvent(QMouseEvent *);

private:
    QRadioButton(const QRadioButton &);
};
