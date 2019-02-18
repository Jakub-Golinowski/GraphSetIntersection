CXX = g++ -std=c++11
CXXFLAGS += -O3 -Wall -Wno-unused-result -mavx2 -lmetis -pthread

# SOURCES = $(shell find . | grep -e ".cpp" | grep -v "tc.cpp" | grep -v "reorder.cpp"| grep -v "mc.cpp")
# OBJECTS = $(SOURCES:%.cpp=%.o)
SOURCES = $(shell find . | grep -e ".hpp")
OBJECT_NAMES_WITH_PREFIX = $(SOURCES:%.hpp=%.o)
OBJECT_NAMES = $(OBJECT_NAMES_WITH_PREFIX:./%=%)
OBJECT_NAMES := $(OBJECT_NAMES) roaring.o

BUILD=../build/
BIN=../bin/
SOURCE=./

$(shell mkdir -p $(BUILD))
$(shell mkdir -p $(BUILD)/exp)
$(shell mkdir -p $(BIN))
$(shell mkdir -p $(HOME)/bin)

OBJECTS=$(addprefix $(BUILD)/, $(OBJECT_NAMES))

all: tc mc sm reorder test_intersection_algos

tc: $(OBJECTS) tc.cpp
	$(CXX) $^ $(CXXFLAGS) -o $(BIN)/$@

mc: $(OBJECTS) mc.cpp
	$(CXX) $^ $(CXXFLAGS) -o $(BIN)/$@

sm: $(OBJECTS) sm.cpp
	$(CXX) $^ $(CXXFLAGS) -o $(BIN)/$@

reorder: $(OBJECTS) reorder.cpp
	$(CXX) $^ $(CXXFLAGS) -o $(BIN)/$@

test_intersection_algos: $(OBJECTS) $(SOURCE)/exp/test_intersection_algos.cpp
	$(CXX) $^ $(CXXFLAGS) -o $(BIN)/$@

$(BUILD)/%.o: $(SOURCE)/%.cpp $(SOURCE)/%.hpp $(SOURCE)/util.hpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

$(BUILD)/roaring.o: $(SOURCE)/roaring/roaring.c $(SOURCE)/roaring/roaring.h $(SOURCE)/roaring/roaring.hh
	$(CXX) $(CXXFLAGS) -c $< -o $@

clean:
	rm -rf $(BIN)/tc $(BIN)/mc $(BIN)/sm $(BIN)/reorder $(BIN)/test_intersection_algos $(OBJECTS)

install: $(shell find $(BIN) -type f)
	install $^  $(HOME)/bin/
