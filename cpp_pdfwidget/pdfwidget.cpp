#include "pdfwidget.h"
#include <poppler-qt4.h>
#include <QAction>
#include <QPixmap>

PdfWidget::PdfWidget(QString path, QWidget *parent)
		: QLabel(parent), path(path)
{
	doc = Poppler::Document::load(path);
	doc->setRenderHint(Poppler::Document::TextAntialiasing);
	n_pages = doc->numPages();
	current_page = 0;
	load_current_page();

	QAction *next_page = new QAction("Next Page", this);
	next_page->setShortcut(Qt::Key_Right);
	connect(next_page, SIGNAL(triggered()), this, SLOT(next_page()));
	addAction(next_page);

	QAction *prev_page = new QAction("Prev Page", this);
	prev_page->setShortcut(Qt::Key_Left);
	connect(prev_page, SIGNAL(triggered()), this, SLOT(prev_page()));
	addAction(prev_page);
}

void PdfWidget::next_page()
{
	current_page++;
	if(current_page >= n_pages) current_page = 0;
	load_current_page();
}

void PdfWidget::prev_page()
{
	if(current_page) current_page--;
	else current_page = n_pages - 1;
	load_current_page();
}

void PdfWidget::load_current_page()
{
	setPixmap(QPixmap::fromImage(doc->page(current_page)->renderToImage()));
	setWindowTitle(QString("%1/%2 - %3").arg(current_page+1)
	                                    .arg(n_pages).arg(path));
}
