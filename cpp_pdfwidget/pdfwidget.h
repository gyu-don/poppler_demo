#include <QLabel>
#include <QString>

namespace Poppler{
	class Document;
};

class PdfWidget : public QLabel{
	Q_OBJECT
public:
	PdfWidget(QString path, QWidget *parent = 0);
public slots:
	void next_page();
	void prev_page();
private:
	void load_current_page();
	int n_pages;
	int current_page;
	QString path;
	Poppler::Document *doc;
};
