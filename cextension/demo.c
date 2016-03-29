
#include <Python.h>

// No argument. Return string.
static PyObject* mynoargfunc(PyObject* self)
{
	return Py_BuildValue("s", "Hello, Python extensions!!");
}

// 3 argument; without return.
static PyObject *argument_test(PyObject *self, PyObject *args) {
	int i;
	double d;
	char *s;

	if (!PyArg_ParseTuple(args, "ids", &i, &d, &s)) {
		return NULL;
	}
	printf("What we get: int=%d float=%f str=%s\n", i, d, s);

	/* Do something interesting here. */
	Py_RETURN_NONE;
}

// Return integer
static PyObject *my_add_test(PyObject *self, PyObject *args)
{
	int a;
	int b;

	if (!PyArg_ParseTuple(args, "ii", &a, &b)) {
		return NULL;
	}
	return Py_BuildValue("i", a + b);
}

// Return tuple
static PyObject *list_test(PyObject *self)
{
	return Py_BuildValue("(s,i)", "string", 3);
}

// Return list
static PyObject *varlist_test(PyObject *self)
{
	PyObject *varlist = PyList_New(0);

	PyList_Append(varlist, PyInt_FromLong(1));
	PyList_Append(varlist, PyUnicode_FromString("str"));

	return varlist;
}

static PyObject *varcomplex_test(PyObject *self)
{
	PyObject *dicttmp = PyDict_New();
	PyObject *varlist = PyList_New(0);

	PyList_Append(varlist, PyInt_FromLong(1));
	PyList_Append(varlist, PyUnicode_FromString("str"));

	PyDict_SetItemString(dicttmp, "thisislist", varlist);

	return dicttmp;
}

static char cextension_docs[] = "Any message you want to put here!!\n";

static PyMethodDef cextension_funcs[] = {
	{	"noargfunc", (PyCFunction)mynoargfunc, METH_NOARGS, cextension_docs},
	{	"argument_test", (PyCFunction)argument_test, METH_VARARGS, NULL },
	{	"foo_add", (PyCFunction)my_add_test, METH_VARARGS, NULL },
	{	"list_test", (PyCFunction)list_test, METH_NOARGS, NULL },
	{	"varlist_test", (PyCFunction)varlist_test, METH_NOARGS, NULL },
	{	"varcomplex_test", (PyCFunction)varcomplex_test, METH_NOARGS, NULL },
	{NULL}
	};


void initcextension(void)
{
	Py_InitModule3("cextension", cextension_funcs, "Extension module example!");
}







